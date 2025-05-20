
<p align="center">
  <a href="https://www.uit.edu.vn/" title="Trường Đại học Công nghệ Thông tin" style="border: 5;">
    <img src="https://i.imgur.com/WmMnSRt.png" alt="Trường Đại học Công nghệ Thông tin | University of Information Technology">
  </a>
</p>

<!-- Title -->
<h1 align="center"><b>CS317.P21 - PHÁT TRIỂN VÀ VẬN HÀNH HỆ THỐNG MÁY HỌC</b></h1>

## Môn học 
<a name="gioithieumonhoc"></a>
* *Môn học*: Phát triển và vận hành hệ thống máy học
* *Mã lớp*: CS317.P21
* *Year*: 2024-2025
## Giáo viên
<a name="giangvien"></a>
* *Đỗ Văn Tiến* - tiendv@uit.edu.vn
* *Lê Trần Trọng Khiêm* - khiemltt@uit.edu.vn

## Danh sách thành viên:
| Họ và tên      | MSSV | Lớp     |
| :----:        |    :----:   |          :----: |
| [Phạm Huỳnh Nhật Tân](https://github.com/tanphn?tab=repositories)      | 22521309       | CS317.P21  |
| [Phạm Nguyễn Anh Tuấn](https://github.com/nguoimay1103?tab=repositories)   | 22521610        | CS317.P21     |
| [Nguyễn Dương Quốc Thắng](https://github.com/solohito?tab=repositories)   | 22521332       | CS317.P21     |
| [Ngô Nguyễn Nam Trung](https://github.com/namtrunguit?tab=repositories)   | 22521559      | CS317.P21     |

# CS317: Lab 2 – API, Docker and Deploy API
Đây là project triển khai mô hình học sâu đã xây dựng ở Lab 1 dưới dạng REST API bằng FastAPI.  
Ứng dụng được đóng gói bằng Docker và có thể deploy dễ dàng chỉ với một lệnh `docker-compose`.
1. ### `Cài đặt thư viện`
```bash
pip install -r requirements.txt
```
2. ### `Tạo API với FastAPI`
```bash
uvicorn main:app --reload
```
3. ### `Xây dựng docker image local`
```bash
docker build -t demo:latest .
docker run -d -p 8000:8080 demo:latest
```
4. ### `Xây dựng docker compse local`
   * Yêu cầu: docker-compose.yaml file
```bash
docker-compose up --build
```
5. ### `Chạy demo API`
   - Truy cập:  http://0.0.0.0:8080/docs để thử demo FASTAPI
## **Video trình bày kết quả**
  Video demo: **https://youtu.be/P1jXfmg_znQ?si=L0l1PYWCKaDeGIwr**
## **Push image đã build lên Docker hub**
```bash
docker pull nguoimay1103/cs317_lab2:latest
```
<div align="center">
    <img src="https://github.com/user-attachments/assets/2ed7753e-8e14-4b23-92be-b5e428953632" width="600"/>
</div>
