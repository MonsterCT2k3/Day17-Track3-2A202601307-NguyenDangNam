# Lab 17 — Submission: Multi-Memory Agent

> **Nguyễn Đăng Nam** — MSSV 2A202601307

## 1. Lý thuyết & kiến trúc

**Layer quan trọng nhất trong bộ test này:** `Long-term` — 20/56 điểm, 4/11 case (**E02, E03, E08, E09**): giữ sở thích qua phiên (E02 Python), theo dõi open-loop (E03 deadline 16:00), xử lý recency (E08 BLUEBIRD-42), cô lập user (E09 Lan không thấy dữ liệu Minh).

**Trade-off Zep Cloud vs Redis+Qdrant:** Zep V3 cho sẵn Context Block đa phiên, trích xuất thực thể, temporal validity, user isolation; đổi lại phụ thuộc dịch vụ ngoài và latency mạng (~2s/case). Redis+Qdrant chạy dưới 1ms, dữ liệu tại local, chi phí cố định, nhưng phải tự code trích xuất graph, merge ngữ cảnh, giải quyết xung đột khi fact cập nhật.

**Guardrail chống memory poisoning:** gắn provenance `source`/`thread_id`, kiểm tra consent trước khi ghi durable memory; tầng policy không bị prune hay ghi đè bởi input người dùng; redact PII qua `privacy_guard.py`; `heartbeat` chỉ được dọn/gộp, không cấp quyền mới.

## 2. Benchmark

1. **Layer yếu nhất ở baseline:** no-memory 0% ở cả Long-term, Episodic, Semantic (fail 9/11); chỉ short-term PASS vì bằng chứng còn trong thread hiện tại. Student: 11/11.
2. **Tốn token nhất:** E03 (1413) và E02 (1398) — Long-term nạp cả Context Block lẫn fact-search audit.
3. **E07 mixed:** Long-term (Python của Minh) + Semantic (`Idempotency-Key` từ KB chung `kb-payment-retry`).
4. **Token reduction vs hit rate:** no-memory giảm 81.8% token nhưng chỉ 18.2% hit rate — không nạp gì thì rẻ mà sai. Student giảm 67.8–74.2% ở semantic vẫn 100% hit rate nhờ trích đúng bằng chứng.

## 3. E08 recency & E10 compaction

**E08:** Minh khai Python trước, sau đó chốt BLUEBIRD-42 dùng TypeScript/NestJS. Zep gắn khoảng hiệu lực cho từng edge nên fact mới vô hiệu hoá fact cũ **trong phạm vi dự án đó** (thấy rõ `invalid_at` ở `ui_chat.png`); E02 vẫn giữ Python ở phạm vi cá nhân.

**E10:** Sliding window chỉ giữ N lượt cuối, nhưng `extract_durable_notes` bắt từ khoá ràng buộc và marker in hoa nên đẩy `REVIEW-DEADLINE-1600 / Friday / 16:00` vào `durable_notes` trước khi cắt. Hạ `max_recent_messages` 6→4 làm tăng số lần compaction mà deadline vẫn còn: được quên lượt thoại, không được quên ràng buộc.

## 4. Minh chứng

`submission/long_term.png` (E02/E03/E08/E09) · `episodic.png` (E04/E05) · `semantic.png` (E06/E11) · `privacy.png` (forget + verify) · `ui.png` + `ui_chat.png` (UI demo E07: evidence per-layer, chat cite PAYMENT-RULE-3)
