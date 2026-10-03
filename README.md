# Page Source Fetcher

سكريبت بايثون بيفتح أي صفحة بمتصفح حقيقي (Playwright) ويحفظ كودها:

- `rendered.html`: الكود بعد تشغيل الـ JavaScript
- `raw.html`: الكود الأصلي من السيرفر

## التثبيت

```bash
pip install playwright
playwright install chromium
```

## الاستخدام

1. غيّر `SITE` في السكريبت إلى الرابط المطلوب.
2. شغّله:

```bash
python get_source.py
```

