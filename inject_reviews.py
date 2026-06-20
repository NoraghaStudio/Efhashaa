import json
import re

def main():
    try:
        # Load reviews
        with open('extracted_reviews.json', 'r', encoding='utf-8') as f:
            reviews = json.load(f)
            
        print(f"Loaded {len(reviews)} reviews.")

        # Read index.html
        with open('index.html', 'r', encoding='utf-8') as f:
            html = f.read()

        # Generate JS snippet
        reviews_json = json.dumps(reviews, ensure_ascii=False)
        
        js_code = f"""
            <div class="reviews-grid" id="haraj-reviews-grid" style="max-height: 800px; overflow-y: auto; padding: 10px; direction: rtl;">
                <!-- Reviews injected via JS -->
            </div>
            
            <script>
                document.addEventListener('DOMContentLoaded', () => {{
                    const reviews = {reviews_json};
                    const grid = document.getElementById('haraj-reviews-grid');
                    
                    const starsSvg = `
                        <div class="review-stars">
                            <svg width="20" height="20" fill="currentColor" viewBox="0 0 24 24"><path d="M12 2l3.09 6.26L22 9.27l-5 4.87 1.18 6.88L12 17.77l-6.18 3.25L7 14.14 2 9.27l6.91-1.01L12 2z"/></svg>
                            <svg width="20" height="20" fill="currentColor" viewBox="0 0 24 24"><path d="M12 2l3.09 6.26L22 9.27l-5 4.87 1.18 6.88L12 17.77l-6.18 3.25L7 14.14 2 9.27l6.91-1.01L12 2z"/></svg>
                            <svg width="20" height="20" fill="currentColor" viewBox="0 0 24 24"><path d="M12 2l3.09 6.26L22 9.27l-5 4.87 1.18 6.88L12 17.77l-6.18 3.25L7 14.14 2 9.27l6.91-1.01L12 2z"/></svg>
                            <svg width="20" height="20" fill="currentColor" viewBox="0 0 24 24"><path d="M12 2l3.09 6.26L22 9.27l-5 4.87 1.18 6.88L12 17.77l-6.18 3.25L7 14.14 2 9.27l6.91-1.01L12 2z"/></svg>
                            <svg width="20" height="20" fill="currentColor" viewBox="0 0 24 24"><path d="M12 2l3.09 6.26L22 9.27l-5 4.87 1.18 6.88L12 17.77l-6.18 3.25L7 14.14 2 9.27l6.91-1.01L12 2z"/></svg>
                        </div>
                    `;

                    const html = reviews.map(r => `
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
                    
                    grid.innerHTML = html;
                }});
            </script>
        """

        # We will replace the <div class="reviews-grid">...</div> block in Haraj reviews
        # We need a regex that matches from <div class="reviews-grid"> up to exactly before the <div style="text-align: center; margin-top: 40px;">
        # inside the #haraj-reviews section.
        
        pattern = re.compile(r'<section class="reviews-section" id="haraj-reviews">.*?<div class="reviews-grid">.*?(?=<div style="text-align: center; margin-top: 40px;">\s*<a href="https://haraj\.com)', re.DOTALL)
        
        replacement = f"""<section class="reviews-section" id="haraj-reviews">
        <div class="container">
            <div class="section-header">
                <h2>آراء عملاء حراج</h2>
                <p class="section-desc">شهادات نعتز بها من عملائنا في منصة حراج</p>
            </div>
            
{js_code}
            """
            
        if pattern.search(html):
            new_html = pattern.sub(replacement, html)
            with open('index.html', 'w', encoding='utf-8') as f:
                f.write(new_html)
            print("Successfully injected all reviews into index.html")
        else:
            print("Could not find the target HTML block to replace.")

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
