# VN30 Streamlit App

Ứng dụng Streamlit cho phép tải dữ liệu CSV đã xử lý lên, phân cụm K-Means theo:
- 3 biến: `relative_resilience`, `recovery_ratio_60d`, `resilience`
- 5 biến: `volatility_60d`, `mean_return_60d`, `momentum_60d`, `avg_volume_60d`, `beta`

## Chạy thử trên máy
```bash
pip install -r requirements.txt
streamlit run app.py
```

## Triển khai trên Streamlit Community Cloud
1. Đưa `app.py` và `requirements.txt` lên repository GitHub.
2. Vào https://share.streamlit.io/ và chọn repository.
3. Chọn branch `main` (hoặc branch mặc định) và Main file path `app.py`.
4. Deploy.
5. Khi ứng dụng chạy, tải lên CSV đã xử lý, ví dụ `df_scaled.csv`.

Lưu ý: `models.pkl` đã tạo trước đó chỉ chứa nội dung của 5 file nguồn, không phải mô hình Machine Learning đã huấn luyện. Ứng dụng này chạy K-Means trực tiếp trên CSV người dùng tải lên.
