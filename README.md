# 📈 NHÓM 10 ML — PHỤC HỒI VÀ CHỐNG CHỊU CỔ PHIẾU VN30

<p align="center">
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/Machine%20Learning-FF6F00?style=for-the-badge&logo=scikitlearn&logoColor=white" />
  <img src="https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white" />
  <img src="https://img.shields.io/badge/Market-VN30-0B8457?style=for-the-badge" />
</p>

<p align="center">
  <b>ỨNG DỤNG HỌC MÁY ĐÁNH GIÁ KHẢ NĂNG CHỐNG CHỊU VÀ PHỤC HỒI CỦA CỔ PHIẾU</b>
  <br/>
  <i>Bằng chứng thực nghiệm từ rổ chỉ số VN30 giai đoạn 2018–2026</i>
</p>

---

## 🌟 1. Giới thiệu dự án

Dự án ứng dụng các phương pháp phân tích dữ liệu và học máy (*Machine Learning*) nhằm đánh giá khả năng chống chịu trước những cú sốc thị trường và khả năng phục hồi của các cổ phiếu thuộc VN30.

Trong bối cảnh thị trường chứng khoán Việt Nam chịu ảnh hưởng từ đại dịch COVID-19, biến động kinh tế vĩ mô và những thay đổi trong chính sách tiền tệ, việc nhận diện các cổ phiếu có đặc điểm chống chịu tốt và phục hồi nhanh có ý nghĩa quan trọng đối với phân tích rủi ro và hỗ trợ ra quyết định đầu tư.

### 🎯 Mục tiêu

- 📊 Thu thập và xử lý dữ liệu giá cổ phiếu VN30 giai đoạn 2018–2026.
- 🔍 Xây dựng các chỉ tiêu đo lường khả năng chống chịu và phục hồi.
- 🤖 Ứng dụng thuật toán phân cụm để nhận diện các nhóm cổ phiếu có đặc điểm tương đồng.
- 📈 Trực quan hóa kết quả và hỗ trợ so sánh đặc điểm giữa các nhóm cổ phiếu.
- 💡 Cung cấp thêm thông tin phục vụ nghiên cứu và quản trị rủi ro đầu tư.

## 🧠 2. Phương pháp thực hiện

| Giai đoạn | Nội dung |
|---|---|
| 01 — Data Collection | Thu thập dữ liệu giá cổ phiếu |
| 02 — Data Preprocessing | Làm sạch, xử lý dữ liệu thiếu và chuẩn hóa |
| 03 — Feature Engineering | Xây dựng chỉ tiêu chống chịu và phục hồi |
| 04 — Machine Learning | Phân cụm cổ phiếu dựa trên các đặc trưng đã lựa chọn |
| 05 — Evaluation | Đánh giá chất lượng phân cụm |
| 06 — Visualization | Xây dựng biểu đồ và ứng dụng tương tác bằng Streamlit |

*Lưu ý: Thuật toán và số lượng cụm cuối cùng cần được xác định theo mô hình thực tế được sử dụng trong dự án.*

## 🛠️ 3. Công nghệ sử dụng

- **Python:** Ngôn ngữ lập trình chính.
- **Pandas & NumPy:** Xử lý và tính toán dữ liệu.
- **Scikit-learn:** Chuẩn hóa dữ liệu, xây dựng và đánh giá mô hình học máy.
- **Matplotlib, Seaborn & Plotly:** Trực quan hóa dữ liệu.
- **Streamlit:** Xây dựng giao diện ứng dụng phân tích tương tác.
- **Joblib / Pickle:** Lưu và tải lại mô hình đã huấn luyện.
- **VNStock:** Hỗ trợ thu thập dữ liệu chứng khoán Việt Nam khi cần thiết.

## 📂 4. Cấu trúc dự án

```text
VN30-Resilience/
│
├── requirements.txt                 # Danh sách thư viện
├── README.md                        # Tài liệu dự án
│
├── data/
│   ├── unprocessed/                 # Dữ liệu ban đầu
│   └── processed/                   # Dữ liệu đã xử lý
│
├── notebooks/
│   └── 1.0-EDA.ipynb                # Phân tích khám phá dữ liệu
│   └── 2.0-model-prototyping.ipynb  # Thử nghiệm, so sánh mô hình  
├── src/
|   |__ data_preparation.py          # Hàm chuẩn bị dataset hoàn chỉnh
|   |__ data_processing.py           # Hàm tiền xử lý dữ liệu
│   |__ train_f5                     # Script huấn luyện mô hình 5 biến đặc trưng
|   |__ train_f3                     # Script huấn luyện mô hình 3 biến đặc trưng
|__models/                           # Chứa file mô hình đã train
|__reports/
    |__figures/                      # Biểu đồ, hình ảnh
```


## ⚙️ 5. Cài đặt và khởi chạy

### Bước 1. Sao chép repository

```bash
git clone <GITHUB_REPOSITORY_URL>
cd VN30-Resilience
```

Thay `<GITHUB_REPOSITORY_URL>` bằng đường dẫn GitHub của dự án.

### Bước 2. Tạo môi trường ảo (khuyến nghị)

```bash
python -m venv .venv
```

Kích hoạt trên Windows:

```bash
.venv\Scripts\activate
```

### Bước 3. Cài đặt thư viện

```bash
python -m pip install -r requirements.txt
```

### Bước 4. Chạy ứng dụng

```bash
streamlit run app.py
```

Sau khi khởi chạy, mở địa chỉ local được hiển thị trong Terminal để sử dụng ứng dụng.

## 📊 6. Nội dung phân tích

Ứng dụng hướng đến các chức năng sau:

- **Tổng quan dữ liệu:** Thống kê dữ liệu và đặc điểm của các cổ phiếu.
- **Phân tích biến động:** Quan sát diễn biến giá và lợi suất theo thời gian.
- **Đánh giá chống chịu:** Phân tích mức độ suy giảm của cổ phiếu trong các giai đoạn thị trường bất lợi.
- **Đánh giá phục hồi:** Theo dõi khả năng lấy lại mức giá trước cú sốc và thời gian phục hồi.
- **Phân cụm cổ phiếu:** Nhận diện các nhóm có đặc điểm tương đồng dựa trên các chỉ tiêu đầu vào.
- **Trực quan hóa:** Hiển thị biểu đồ, bảng kết quả và thông tin chi tiết theo mã cổ phiếu.

*Các chức năng cần được triển khai và đối chiếu với dữ liệu thực tế trước khi công bố.*

## 🚀 7. Triển khai trực tuyến

Dự án có thể được triển khai bằng Streamlit Community Cloud.

1. Đưa mã nguồn lên GitHub.
2. Đảm bảo repository có file `app.py` và `requirements.txt`.
3. Truy cập [Streamlit Community Cloud](https://share.streamlit.io/).
4. Kết nối GitHub và chọn repository.
5. Chọn nhánh chứa mã nguồn và file khởi chạy `app.py`.
6. Nhấn **Deploy** để triển khai ứng dụng.

## 📌 8. Ý nghĩa thực tiễn

Kết quả nghiên cứu có thể hỗ trợ:

- Nhận diện sự khác biệt về khả năng chống chịu giữa các cổ phiếu.
- So sánh tốc độ và mức độ phục hồi sau các giai đoạn biến động.
- Hỗ trợ nghiên cứu chiến lược quản trị rủi ro và xây dựng danh mục đầu tư.
- Minh họa khả năng ứng dụng học máy trong phân tích thị trường chứng khoán Việt Nam.

Kết quả phân cụm phản ánh đặc điểm của dữ liệu và các chỉ tiêu được lựa chọn, không đảm bảo khả năng dự báo lợi nhuận trong tương lai.

## 👥 9. Thông tin nhóm thực hiện

- **Nhóm:** Nhóm 10 ML
- **Đề tài:** Ứng dụng học máy đánh giá khả năng chống chịu và phục hồi của cổ phiếu VN30
- **Thời gian nghiên cứu:** 2018–2026
- **Ngôn ngữ:** Python
- **Nền tảng triển khai:** Streamlit

*Bổ sung họ tên thành viên, lớp, giảng viên hướng dẫn và thông tin liên hệ theo yêu cầu của học phần.*

---

<p align="center">
  <b>📈 NHÓM 10 ML — DATA • MACHINE LEARNING • FINANCIAL RESILIENCE</b>
  <br/>
  
  <i> Phân tích dữ liệu hôm nay — Hiểu rõ rủi ro ngày mai.</i>
</p>
