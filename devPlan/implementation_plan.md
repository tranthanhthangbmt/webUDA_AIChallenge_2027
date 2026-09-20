# Kế hoạch Xây dựng Website UDA AI Challenge 2027

Website sẽ được xây dựng để cung cấp thông tin, hỗ trợ đăng ký và cung cấp tài liệu tập huấn (Bootcamp) cho sinh viên tham gia cuộc thi AI Innovation Challenge. Website sẽ được thiết kế với giao diện sáng sủa, hiện đại, và tối ưu hóa để triển khai lên GitHub Pages.

## Dự án sẽ được khởi tạo trong thư mục webUDA_AIChallenge_2027.

### Khởi tạo Dự án
Sử dụng Vite để khởi tạo dự án với template Vanilla JS:
- Khởi tạo cấu trúc Vite.
- Thiết lập thư mục public/ và src/ (css, js, assets).

### Cấu trúc Giao diện (Pages & Sections)
Website sẽ là một trang Single Page Application (hoặc Landing Page) có các phân vùng:
1. Hero Section: Tiêu đề "UDA AI Innovation Challenge 2027", thông điệp chính và nút Call-to-action (Đăng ký).
2. Về Cuộc thi (About): Giới thiệu kiến trúc 4 tầng công nghệ (NotebookLM, Gemini, n8n, Antigravity).
3. Các Phân ban (Tracks): 
   - Smart Campus
   - Tourism
   - Agriculture
   - Healthcare & Community
4. Lộ trình (Roadmap): 
   - Tuần 1: Phát động
   - Tuần 2-3: Bootcamp (Tài liệu tập huấn sẽ được đính kèm ở đây)
   - Tuần 4: Sơ khảo
   - Tuần 5: Chung kết & Demo Day
5. Đăng ký (Register): Nút đăng ký và thông tin liên hệ Ban tổ chức.

### CSS & UI Design
- Font chữ: Inter hoặc Outfit từ Google Fonts.
- Hiệu ứng: Sử dụng micro-animations, glassmorphism cho các card thông tin, hover effect mượt mà.
- Phối màu: Sáng sủa (Sắc trắng/bạc làm nền, chữ xám đậm/đen, điểm xuyết màu Xanh dương và Cam năng động).

## Verification Plan

### Automated Tests
- Kiểm tra build thành công bằng lệnh npm run build.
- Đảm bảo không có lỗi CSS hay JS trong quá trình build.

### Manual Verification
- Chạy npm run dev để kiểm tra giao diện trên trình duyệt (Responsive trên Mobile và Desktop).
- Đảm bảo các nút điều hướng cuộn đúng đến các phần tương ứng.
- Hướng dẫn người dùng push code lên GitHub và cấu hình GitHub Pages từ nhánh main (hoặc gh-pages).
