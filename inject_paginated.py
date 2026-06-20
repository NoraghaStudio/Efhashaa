import json
import re

def main():
    try:
        # Load reviews
        with open('extracted_reviews.json', 'r', encoding='utf-8') as f:
            reviews = json.load(f)

        # Read index.html
        with open('index.html', 'r', encoding='utf-8') as f:
            html = f.read()

        reviews_json = json.dumps(reviews, ensure_ascii=False)
        
        js_code = f"""
            <div class="reviews-grid" id="haraj-reviews-grid" style="direction: rtl;">
                <!-- Reviews injected via JS -->
            </div>
            
            <div style="text-align: center; margin-top: 40px; display: flex; gap: 15px; justify-content: center; flex-wrap: wrap;">
                <button id="load-more-reviews" class="cta-btn cta-primary" style="cursor: pointer; border: none; font-family: inherit;">عرض المزيد من التقييمات</button>
                <a href="https://haraj.com.sa/users/%D8%A7%D9%81%D8%AD%D8%B5%20%D9%87%D8%A7" target="_blank" class="cta-btn cta-secondary">حسابنا في حراج</a>
            </div>
            
            <script>
                document.addEventListener('DOMContentLoaded', () => {{
                    const reviews = {reviews_json};
                    const grid = document.getElementById('haraj-reviews-grid');
                    const loadMoreBtn = document.getElementById('load-more-reviews');
                    let currentIndex = 0;
                    const reviewsPerLoad = 6;
                    
                    const starsSvg = `
                        <div class="review-stars">
                            <svg width="20" height="20" fill="currentColor" viewBox="0 0 24 24"><path d="M12 2l3.09 6.26L22 9.27l-5 4.87 1.18 6.88L12 17.77l-6.18 3.25L7 14.14 2 9.27l6.91-1.01L12 2z"/></svg>
                            <svg width="20" height="20" fill="currentColor" viewBox="0 0 24 24"><path d="M12 2l3.09 6.26L22 9.27l-5 4.87 1.18 6.88L12 17.77l-6.18 3.25L7 14.14 2 9.27l6.91-1.01L12 2z"/></svg>
                            <svg width="20" height="20" fill="currentColor" viewBox="0 0 24 24"><path d="M12 2l3.09 6.26L22 9.27l-5 4.87 1.18 6.88L12 17.77l-6.18 3.25L7 14.14 2 9.27l6.91-1.01L12 2z"/></svg>
                            <svg width="20" height="20" fill="currentColor" viewBox="0 0 24 24"><path d="M12 2l3.09 6.26L22 9.27l-5 4.87 1.18 6.88L12 17.77l-6.18 3.25L7 14.14 2 9.27l6.91-1.01L12 2z"/></svg>
                            <svg width="20" height="20" fill="currentColor" viewBox="0 0 24 24"><path d="M12 2l3.09 6.26L22 9.27l-5 4.87 1.18 6.88L12 17.77l-6.18 3.25L7 14.14 2 9.27l6.91-1.01L12 2z"/></svg>
                        </div>
                    `;

                    const renderReviews = (startIndex, count) => {{
                        const chunk = reviews.slice(startIndex, startIndex + count);
                        const html = chunk.map(r => `
                            <div class="review-card">
                                <div class="review-header">
                                    ${{starsSvg}}
                                    <img src="assets/images/haraj.webp" alt="حراج" class="review-source-img">
                                </div>
                                <p class="review-text">"${{r.text}}"</p>
                                <div class="review-footer">
                                    <span class="review-author">${{r.name}}</span>
                                    <span class="review-date">${{r.date}}</span>
                                </div>
                            </div>
                        `).join('');
                        grid.insertAdjacentHTML('beforeend', html);
                        currentIndex += count;
                        
                        if (currentIndex >= reviews.length) {{
                            loadMoreBtn.style.display = 'none';
                        }}
                    }};

                    loadMoreBtn.addEventListener('click', () => {{
                        renderReviews(currentIndex, reviewsPerLoad);
                    }});

                    // Initial load
                    renderReviews(0, reviewsPerLoad);
                }});
            </script>
        """

        # Using regex to replace the specific chunk between <div class="container"> in #haraj-reviews
        # and </section> for haraj-reviews.
        pattern = re.compile(r'(<section class="reviews-section" id="haraj-reviews">.*?<div class="container">.*?<p class="section-desc">شهادات نعتز بها من عملائنا في منصة حراج</p>\s*</div>\s*)(.*?)(?=\s*</section>)', re.DOTALL)
        
        if pattern.search(html):
            new_html = pattern.sub(r'\1\n' + js_code.replace('\\', '\\\\') + r'\n', html)
            with open('index.html', 'w', encoding='utf-8') as f:
                f.write(new_html)
            print("Successfully injected paginated reviews!")
        else:
            print("Regex pattern not found.")

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
