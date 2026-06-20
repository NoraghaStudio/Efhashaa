import os
import re

# 1. Copy and modify style.css
with open('/home/bin-naqeeb/Documents/AbuRayyan/style.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Replace Gold with Blue
css = css.replace('--gold: #c8a456;', '--gold: #1e3a8a;')
css = css.replace('--gold-light: #e0c478;', '--gold-light: #3b82f6;')
css = css.replace('--gold-dark: #a8873a;', '--gold-dark: #1e40af;')
# Replace RGB values of gold (200,164,86) with blue (30,58,138)
css = css.replace('200,164,86', '30,58,138')
css = css.replace('200, 164, 86', '30, 58, 138')

with open('/home/bin-naqeeb/Documents/Efhashaa/style.css', 'w', encoding='utf-8') as f:
    f.write(css)

# 2. Build index.html
html_content = """<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>تقرير موجز | فحص سيارات وتشيك استدعاءات</title>
    <meta name="description" content="تقرير موجز بملف pdf مع شرح صوتي كامل وشامل وفوري. يكشفلك عن تاريخ السياره الكامل ويصلك فوري وسريع.">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=IBM+Plex+Sans+Arabic:wght@300;400;500;600;700&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <!-- Header -->
    <header class="header" id="header" style="background: rgba(10,10,15,0.92); border-bottom: 1px solid var(--border);">
        <div class="container header-inner">
            <div class="logo-area">
                <img src="assets/images/logo-ar.jpeg" alt="شعار" style="height: 40px; border-radius: 8px;">
                <span class="logo-text" style="font-weight: 700; color: #fff; font-size: 1.15rem; font-family: 'IBM Plex Sans Arabic', sans-serif; margin-right: 10px;">
                    تقرير <span style="color: var(--gold);">موجز</span>
                </span>
            </div>
            <a href="https://wa.me/966598830561" class="cta-btn header-cta" dir="ltr" target="_blank">
                <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                    <path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72c.127.96.361 1.903.7 2.81a2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45c.907.339 1.85.573 2.81.7A2 2 0 0 1 22 16.92z" />
                </svg>
                0598830561
            </a>
        </div>
    </header>

    <!-- Hero Section -->
    <section class="hero" id="hero" style="background: url('assets/images/efhashaa.jpeg') center/cover no-repeat; min-height: 100vh;">
        <div class="hero-bg-overlay"></div>
        <div class="container hero-content">
            <img src="assets/images/Mojaz.webp" alt="تقرير موجز" class="hero-main-logo" style="background: white; padding: 10px;">
            <h1>تـــــقـــريـــــر <span style="color: var(--gold);">مــــــوجــــــز</span><br>
                <span style="display: block; font-size: 1.4rem; font-weight: 500; color: var(--gold); margin-top: 12px; line-height: 1.6;">
                    مع شرح صوتي كامل وشامل وفوري
                </span>
            </h1>
            <p class="hero-desc">
                يكشف لك عن تاريخ السياره الكامل ويصلك تقرير موجز فوري وسريع خلال دقيقه فقط من بعد التحويل نحن اسرع حتى من التطبيق.
            </p>

            <div class="hero-actions">
                <a href="https://wa.me/966598830561" class="cta-btn cta-whatsapp cta-large" target="_blank">
                    تواصل واتساب (اسرع)
                </a>
                <a href="#reports" class="cta-btn cta-secondary cta-large">
                    استكشف محتويات التقرير
                </a>
            </div>
        </div>
    </section>

    <!-- Ticker -->
    <div class="ticker-wrap">
        <div class="ticker">
            <div class="ticker-item">🎉 الوحيد في المملكة الذي يقدم لك خدمة إصدار تقرير موجز مع شرح صوتي والاستشارة فيه من خبير متخصص فحص سيارات 🎉</div>
            <div class="ticker-item">🎉 تشييك الاستدعاء على المركبة هل عليها عيوب مصنعية للوكالة بخدمات مجانية VIP نقدمها للعملاء 🎉</div>
            <div class="ticker-item">🎉 الوحيد في المملكة الذي يقدم لك خدمة إصدار تقرير موجز مع شرح صوتي والاستشارة فيه من خبير متخصص فحص سيارات 🎉</div>
            <div class="ticker-item">🎉 تشييك الاستدعاء على المركبة هل عليها عيوب مصنعية للوكالة بخدمات مجانية VIP نقدمها للعملاء 🎉</div>
        </div>
    </div>

    <!-- Core Services / Report Content Section -->
    <section class="services-section" id="features">
        <div class="container">
            <div class="section-header">
                <h2>محتويات التقرير</h2>
                <p class="section-desc">جميع المعلومات حسب توفرها من المصدر وقت استخراج التقرير من (المرور، شركة نجم، الفحص الدوري، مركز تقدير، الوكالات، شركة علم)</p>
            </div>
            <div class="services-grid">
                <div class="service-card">
                    <h3>بيانات مواصفات السيارة</h3>
                    <p>معرفة لون السيارة المسجل وعدد الملاك السابقين.</p>
                </div>
                <div class="service-card">
                    <h3>تاريخ الحوادث</h3>
                    <p>معرفة عدد الحوادث وصور لها إن وجدت، وسجلات الصيانة والضمان.</p>
                </div>
                <div class="service-card">
                    <h3>الفحص الدوري والتأمين</h3>
                    <p>تاريخ الفحص والاستمارة وسجلات التأمين واسم الشركة.</p>
                </div>
                <div class="service-card">
                    <h3>العداد</h3>
                    <p>معرفة العداد إذا ملعوب فيه أولاً بشرط دخول الفحص أو الوكالة.</p>
                </div>
                <div class="service-card">
                    <h3>تفاصيل إضافية</h3>
                    <p>عدد التفاويض، أسعار قطع الغيار، وهل كانت لمكتب تأجير.</p>
                </div>
            </div>
        </div>
    </section>

    <!-- Reports Hub Section -->
    <section class="reports-section" id="reports" style="background: var(--bg-surface); padding: 80px 0;">
        <div class="container">
            <div class="section-header">
                <h2>الوحيد المتخصص بإصدار تقارير فحص السيارات بالعالم</h2>
            </div>
            <div class="reports-grid" style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 24px;">
                <div class="service-card" style="background: var(--bg-dark);">
                    <img src="assets/images/Mojaz.webp" alt="Mojaz" style="height: 40px; margin-bottom: 15px; border-radius: 4px;">
                    <h3>تقرير موجز</h3>
                    <p>السعودية (مع شرح صوتي وتشييك الاستدعاءات مجاناً)</p>
                </div>
                <div class="service-card" style="background: var(--bg-dark);">
                    <img src="assets/images/carfax.webp" alt="Carfax" style="height: 40px; margin-bottom: 15px; border-radius: 4px;">
                    <h3>تقرير كارفكس</h3>
                    <p>للسيارات المستوردة من أمريكا</p>
                </div>
                <div class="service-card" style="background: var(--bg-dark);">
                    <img src="assets/images/AutoCheck.webp" alt="AutoCheck" style="height: 40px; margin-bottom: 15px; border-radius: 4px;">
                    <h3>تقرير أوتوشيك</h3>
                    <p>للسيارات المستوردة من كندا</p>
                </div>
                <div class="service-card" style="background: var(--bg-dark);">
                    <img src="assets/images/Carseer.webp" alt="CarSeer" style="height: 40px; margin-bottom: 15px; border-radius: 4px;">
                    <h3>تقرير كارسير</h3>
                    <p>للسيارات المستوردة من أوروبا</p>
                </div>
                <div class="service-card" style="background: var(--bg-dark);">
                    <h3>تقارير كوريا</h3>
                    <p>للسيارات المستوردة من كوريا</p>
                </div>
                <div class="service-card" style="background: var(--bg-dark);">
                    <img src="assets/images/UAE.jpeg" alt="UAE" style="height: 40px; margin-bottom: 15px; border-radius: 4px;">
                    <h3>تقارير الإمارات</h3>
                    <p>تقرير الحوادث فقط للسيارات الواردة من الإمارات</p>
                </div>
            </div>
        </div>
    </section>

    <!-- Trust Stats -->
    <section class="trust-section" id="trust" style="padding: 80px 0;">
        <div class="container">
            <div class="section-header">
                <h2>لماذا تثق بنا !!!</h2>
            </div>
            <div class="trust-stats" style="display: flex; gap: 30px; justify-content: center; flex-wrap: wrap;">
                <div class="stat-item">
                    <span class="stat-number">9</span>
                    <span class="stat-label">سنوات حساب قديم بحراج</span>
                </div>
                <div class="stat-item">
                    <span class="stat-number">700+</span>
                    <span class="stat-label">تقييم ممتاز تبارك الله</span>
                </div>
                <div class="stat-item">
                    <span class="stat-number">أبشر</span>
                    <span class="stat-label">حسابي موثق رسمياً</span>
                </div>
            </div>
            
            <div class="golden-tip" style="margin-top: 40px; background: rgba(30,58,138,0.1); border: 1px solid rgba(30,58,138,0.2); padding: 24px; border-radius: var(--radius); text-align: center;">
                <p style="color: var(--gold); font-size: 1.1rem; font-weight: 600;">السعر شامل الخدمة أرخص سعر في الموقع وحتى أرخص من التطبيق الرسمي!</p>
            </div>
        </div>
    </section>

    <!-- Payment Methods -->
    <section class="pricing-section" id="pricing" style="background: var(--bg-surface); padding: 80px 0;">
        <div class="container">
            <div class="section-header">
                <h2>طرق الدفع المتوفرة</h2>
                <p class="section-desc">سهلناها لك ووفرنا جميع طرق الدفع</p>
            </div>
            <div style="display: flex; flex-wrap: wrap; justify-content: center; gap: 15px; max-width: 800px; margin: 0 auto;">
                <span class="section-badge">محفظة برق</span>
                <span class="section-badge">الراجحي</span>
                <span class="section-badge">العربي</span>
                <span class="section-badge">الرياض</span>
                <span class="section-badge">الأهلي</span>
                <span class="section-badge">الإنماء</span>
                <span class="section-badge">البلاد</span>
                <span class="section-badge">الجزيرة</span>
                <span class="section-badge">انماء باي urpay</span>
                <span class="section-badge">Stc pay</span>
                <span class="section-badge">شحن رصيد موبايلي</span>
            </div>
        </div>
    </section>

    <!-- Footer -->
    <footer class="footer">
        <div class="container">
            <div class="footer-contacts">
                <div class="contact-box">
                    <h3>تواصل معنا وقت ما تبغى التقرير:</h3>
                    <div class="contact-buttons">
                        <a href="https://wa.me/966598830561" class="cta-btn cta-whatsapp" target="_blank" dir="ltr">
                            0598830561
                        </a>
                        <a href="https://x.com/sulimman666" class="cta-btn cta-secondary" target="_blank">تويتر X</a>
                        <a href="https://linktr.ee/cars.vipv" class="cta-btn cta-secondary" target="_blank">Linktree</a>
                        <a href="https://www.mstaml.com/sa/carsvipv" class="cta-btn cta-secondary" target="_blank">مستعمل</a>
                    </div>
                </div>
            </div>
            <div class="footer-bottom">
                <p>© 2026 تقرير موجز - فحص السيارات. لا يسمح بنسخ الإعلان أو حتى جزء منه ويعتبر ملكية فكرية.</p>
            </div>
        </div>
    </footer>

    <!-- Floating WhatsApp -->
    <a href="https://wa.me/966598830561" class="floating-whatsapp" target="_blank" style="position: fixed; bottom: 30px; right: 30px; background: #25d366; color: white; width: 60px; height: 60px; border-radius: 50%; display: flex; align-items: center; justify-content: center; box-shadow: 0 4px 15px rgba(37,211,102,0.4); z-index: 100;">
        <svg width="34" height="34" viewBox="0 0 24 24" fill="currentColor">
            <path d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51-.173-.008-.371-.01-.57-.01-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347m-5.421 7.403h-.004a9.87 9.87 0 01-5.031-1.378l-.361-.214-3.741.982.998-3.648-.235-.374a9.86 9.86 0 01-1.51-5.26c.001-5.45 4.436-9.884 9.888-9.884 2.64 0 5.122 1.03 6.988 2.898a9.825 9.825 0 012.893 6.994c-.003 5.45-4.437 9.884-9.885 9.884m8.413-18.297A11.815 11.815 0 0012.05 0C5.495 0 .16 5.335.157 11.892c0 2.096.547 4.142 1.588 5.945L.057 24l6.305-1.654a11.882 11.882 0 005.683 1.448h.005c6.554 0 11.89-5.335 11.893-11.893a11.821 11.821 0 00-3.48-8.413z" />
        </svg>
    </a>
</body>
</html>
"""

with open('/home/bin-naqeeb/Documents/Efhashaa/index.html', 'w', encoding='utf-8') as f:
    f.write(html_content)

print("Done generating.")
