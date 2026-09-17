# Implementation Notes

## Purchase Order Report

- `res.users.user_signature_image` stores an uploaded signature image and is exposed on the user profile with the image widget.
- Purchase-order and payslip reports render `user_signature_image` as an image with a `140px` height so signatures are readable.
