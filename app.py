import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score, calinski_harabasz_score, davies_bouldin_score
from sklearn.preprocessing import StandardScaler

st.set_page_config(page_title="VN30 - Chống chịu và Phục hồi", page_icon="📈", layout="wide")

st.title("📈 Phân tích khả năng chống chịu và phục hồi cổ phiếu")
st.caption("Ứng dụng học thuật: tải dữ liệu CSV lên để phân cụm và so sánh các cổ phiếu.")

st.info(
    "Tải lên dữ liệu đã xử lý (khuyến nghị df_scaled.csv). "
    "File models.pkl hiện có chỉ là gói nội dung các file nguồn, không phải mô hình đã huấn luyện."
)

uploaded = st.file_uploader("Chọn file dữ liệu CSV", type=["csv"])

if uploaded is not None:
    try:
        df = pd.read_csv(uploaded)
    except Exception as exc:
        st.error(f"Không đọc được CSV: {exc}")
        st.stop()

    st.subheader("1. Tổng quan dữ liệu")
    c1, c2, c3 = st.columns(3)
    c1.metric("Số dòng", f"{len(df):,}")
    c2.metric("Số cột", f"{len(df.columns):,}")
    c3.metric("Số mã cổ phiếu", str(df["ticker"].nunique()) if "ticker" in df.columns else "Không có cột ticker")
    st.dataframe(df.head(20), use_container_width=True)

    resilience_features = ["relative_resilience", "recovery_ratio_60d", "resilience"]
    financial_features = ["volatility_60d", "mean_return_60d", "momentum_60d", "avg_volume_60d", "beta"]

    st.subheader("2. Chọn phương pháp phân tích")
    mode = st.radio(
        "Nhóm biến dùng để phân cụm",
        ["Chống chịu và phục hồi (3 biến)", "Đặc điểm tài chính (5 biến)"],
        horizontal=True
    )
    features = resilience_features if mode.startswith("Chống chịu") else financial_features
    available = [col for col in features if col in df.columns]
    missing = [col for col in features if col not in df.columns]

    if missing:
        st.warning("Dữ liệu đang thiếu các cột cần thiết cho lựa chọn này: " + ", ".join(missing))
        st.write("Các cột có trong file:", ", ".join(map(str, df.columns)))
        st.stop()

    k = st.slider("Số cụm K", min_value=2, max_value=min(10, max(2, len(df) - 1)), value=4)
    scale = st.checkbox("Chuẩn hóa lại các biến trước khi phân cụm", value=True)

    if st.button("Chạy phân cụm K-Means", type="primary"):
        X_df = df[available].apply(pd.to_numeric, errors="coerce").replace([np.inf, -np.inf], np.nan)
        valid_mask = X_df.notna().all(axis=1)
        if valid_mask.sum() <= k:
            st.error(f"Cần nhiều hơn {k} dòng dữ liệu hợp lệ để phân cụm. Hiện có {int(valid_mask.sum())}.")
            st.stop()

        X = X_df.loc[valid_mask].to_numpy(dtype=float)
        if scale:
            X = StandardScaler().fit_transform(X)

        model = KMeans(n_clusters=k, random_state=42, n_init=20)
        labels = model.fit_predict(X)

        result = df.loc[valid_mask].copy()
        result["cluster"] = labels + 1

        st.subheader("3. Kết quả")
        metric_cols = st.columns(4)
        metric_cols[0].metric("Số dòng được phân cụm", f"{len(result):,}")
        metric_cols[1].metric("Số cụm", str(k))
        metric_cols[2].metric("Silhouette", f"{silhouette_score(X, labels):.4f}" if len(set(labels)) > 1 else "N/A")
        metric_cols[3].metric("Inertia (WSS)", f"{model.inertia_:,.3f}")

        st.markdown("**Số lượng cổ phiếu / quan sát trong từng cụm**")
        counts = result["cluster"].value_counts().sort_index().rename_axis("Cụm").to_frame("Số quan sát")
        st.dataframe(counts, use_container_width=True)

        st.markdown("**Giá trị trung bình theo cụm**")
        summary_cols = [c for c in available if c in result.columns]
        summary = result.groupby("cluster")[summary_cols].mean(numeric_only=True).round(4)
        st.dataframe(summary, use_container_width=True)

        if "ticker" in result.columns:
            st.markdown("**Danh sách mã theo cụm**")
            for cluster_id in sorted(result["cluster"].unique()):
                tickers = sorted(result.loc[result["cluster"] == cluster_id, "ticker"].astype(str).unique())
                with st.expander(f"Cụm {cluster_id} ({len(tickers)} mã duy nhất)"):
                    st.write(", ".join(tickers))

        if len(available) >= 2:
            st.markdown("**Biểu đồ phân cụm (hai biến đầu tiên)**")
            fig, ax = plt.subplots()
            scatter = ax.scatter(
                result[available[0]], result[available[1]],
                c=result["cluster"], alpha=0.75
            )
            ax.set_xlabel(available[0])
            ax.set_ylabel(available[1])
            ax.set_title("Kết quả phân cụm K-Means")
            fig.colorbar(scatter, ax=ax, label="Cụm")
            st.pyplot(fig)
            plt.close(fig)

        st.markdown("**Đánh giá bổ sung**")
        if len(set(labels)) > 1 and len(X) > k:
            try:
                st.write({
                    "Calinski-Harabasz": round(calinski_harabasz_score(X, labels), 4),
                    "Davies-Bouldin (càng thấp thường càng tốt)": round(davies_bouldin_score(X, labels), 4),
                })
            except Exception:
                st.caption("Không tính được một số chỉ số đánh giá cho bộ dữ liệu này.")

        csv_bytes = result.to_csv(index=False).encode("utf-8-sig")
        st.download_button(
            "Tải kết quả phân cụm CSV",
            data=csv_bytes,
            file_name="vn30_clustering_results.csv",
            mime="text/csv"
        )
else:
    st.subheader("Cách sử dụng")
    st.markdown(
        "1. Chuẩn bị file CSV có dữ liệu đã xử lý, ví dụ `df_scaled.csv`.\n"
        "2. Tải file lên bằng nút phía trên.\n"
        "3. Chọn nhóm biến và số cụm K.\n"
        "4. Nhấn **Chạy phân cụm K-Means** để xem bảng kết quả, biểu đồ và tải CSV."
    )
    st.caption("Nếu dùng nhóm 3 biến, CSV cần có relative_resilience, recovery_ratio_60d, resilience. "
               "Nếu dùng nhóm 5 biến, CSV cần có volatility_60d, mean_return_60d, momentum_60d, avg_volume_60d, beta.")
