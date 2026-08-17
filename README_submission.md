# Lab 17 - Submission Report: Multi-Memory Agent

> **Học viên:** Nguyễn Đăng Nam  
> **Mã sinh viên:** 2A202601307  
> **Độ dài báo cáo:** < 400 từ.

---

## 1. Phân tích Lý thuyết & Kiến trúc

### Câu 1: Layer quan trọng nhất trong bộ test
- **Tầng quan trọng nhất:** `Long-term Memory` (chiếm 20/56 điểm và 4/11 case: **E02, E03, E08, E09**).
- **Lý do:** Tầng này quyết định khả năng duy trì sở thích người dùng (*E02 Python*), theo dõi nhiệm vụ chưa hoàn thành (*E03 open-loop deadline*), xử lý xung đột cập nhật (*E08 Recency: BLUEBIRD-42 dùng TypeScript*), và ngăn chặn rò rỉ dữ liệu giữa các người dùng (*E09 User Isolation: Lan không thấy dữ liệu của Minh*).

### Câu 2: Đánh đổi (Trade-off) Zep Cloud vs. Redis + Qdrant
- **Zep Cloud V3 (Managed Memory Graph):** Tự động trích xuất thực thể, theo dõi thời gian hiệu lực (*temporal validity*), tổng hợp Context Block đa phiên và cô lập người dùng sẵn có; nhược điểm là phụ thuộc dịch vụ ngoài và độ trễ mạng.
- **Redis + Qdrant (Tự dựng):** Tốc độ cực nhanh (<1ms), kiểm soát toàn bộ dữ liệu tại local, chi phí phần cứng cố định; nhưng tốn rất nhiều công sức để tự code thuật toán trích xuất đồ thị, merge ngữ cảnh và giải quyết xung đột khi thông tin bị thay đổi.

### Câu 3: Guardrail chống nhiễm độc bộ nhớ (Memory Poisoning)
- **Provenance & Verification:** Gắn định danh nguồn (*source/thread_id*) và kiểm tra quyền trước khi nạp vào bộ nhớ bền vững (*durable memory*).
- **Protected Policy Context:** Tầng chính sách an toàn (*Policy Layer*) được bảo vệ tuyệt đối, không bao giờ bị cắt tỉa hay ghi đè bởi thông tin do người dùng nhập vào.
- **Sanitization & Redaction:** Làm mờ dữ liệu nhạy cảm/PII qua `privacy_guard.py` và chỉ cho phép `heartbeat` dọn dẹp (*prune/de-duplicate*) mà không được tự ý cấp quyền mới.

---

## 2. Phân tích Kết quả Benchmark

1. **Layer có hit rate thấp nhất ở baseline:** Trong `No-Memory Baseline`, cả 3 tầng bền vững (`Long-term`, `Episodic`, `Semantic`) đều đạt **0.0% hit rate** (fail 9/11 case) vì không có bộ nhớ ngoài. Trong bài làm `Student Memory`, toàn bộ 4 tầng đều đạt **100% (11/11 PASS)**.
2. **Query tốn token nhất:** Case **E03** (1408 tokens) và **E02** (1402 tokens) do truy vấn tầng Long-term nạp đầy đủ Context Block và fact search audit.
3. **Case Mixed (E07):** Kết hợp **Long-term** (sở thích cá nhân `Python` của Minh) và **Semantic** (quy tắc retry `Idempotency-Key` từ tài liệu dùng chung `kb-payment-retry`).
4. **Token Reduction vs. Hit Rate:** `No-Memory` có mức giảm token cao (81.8%) nhưng hit rate chỉ 18.2% do thiếu ngữ cảnh. `Student Memory` tối ưu giảm token mạnh ở tầng Semantic (giảm 67.8% - 74.2% so với nạp toàn bộ domain docs) mà vẫn đạt **100% hit rate** nhờ trích xuất trúng đích bằng chứng.

---

## 3. Ảnh Chụp Minh chứng Thực nghiệm

- **Long-term PASS (E02, E03, E08, E09):** `submission/long_term.png`
- **Episodic PASS (E04, E05):** `submission/episodic.png`
- **Semantic PASS (E06, E11):** `submission/semantic.png`
- **Privacy Drill (Forget + Verify):** `submission/privacy.png`
