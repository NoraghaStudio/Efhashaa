import re

def migrate():
    with open('admin.html', 'r', encoding='utf-8') as f:
        html = f.read()

    # 1. Remove supabase script tag
    html = re.sub(r'<script src="https://cdn\.jsdelivr\.net/npm/@supabase/supabase-js@2"></script>', '', html)

    # 2. Replace supabase declarations with API_URL
    supabase_decl = r"""<script>\s*const supabaseUrl = '.*?';\s*const supabaseKey = '.*?';\s*const supabaseClient = window\.supabase\.createClient\(supabaseUrl, supabaseKey\);\s*</script>"""
    api_url_decl = """<script>
        const API_URL = 'http://localhost:3000/api';
    </script>"""
    html = re.sub(supabase_decl, api_url_decl, html, flags=re.DOTALL)

    # 3. Replace loadReviews fetch
    load_reviews_old = r"""const \{ data: remoteReviews, error \} = await supabaseClient\s*\.from\('reviews'\)\s*\.select\('\*'\);"""
    load_reviews_new = """const response = await fetch(`${API_URL}/reviews`);
                const error = !response.ok;
                const remoteReviews = error ? null : await response.json();"""
    html = re.sub(load_reviews_old, load_reviews_new, html, flags=re.DOTALL)

    # 4. Replace saveReview update
    save_review_old = r"""const \{ error \} = await supabaseClient\s*\.from\('reviews'\)\s*\.update\(\{ name: newName, text: newText, isHaraj: newIsHaraj \}\)\s*\.eq\('id', id\);"""
    save_review_new = """const response = await fetch(`${API_URL}/reviews/${id}`, {
                    method: 'PUT',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({ name: newName, text: newText, isHaraj: newIsHaraj })
                });
                const error = !response.ok;"""
    html = re.sub(save_review_old, save_review_new, html, flags=re.DOTALL)

    # 5. Replace deleteReview
    delete_old = r"""const \{ error \} = await supabaseClient\.from\('reviews'\)\.delete\(\)\.eq\('id', id\);"""
    delete_new = """const response = await fetch(`${API_URL}/reviews/${id}`, { method: 'DELETE' });
                const error = !response.ok;"""
    html = html.replace(delete_old, delete_new)

    # 6. Replace addHarajReview
    add_old = r"""if \(window\.supabaseClient\) \{\s*const \{ error \} = await supabaseClient\s*\.from\('reviews'\)\s*\.insert\(\[newReview\]\);\s*if \(error\) \{\s*console\.error\("Error inserting Haraj review:", error\);\s*alert\("حدث خطأ أثناء الإضافة\."\);\s*return;\s*\}\s*\}"""
    add_new = """const response = await fetch(`${API_URL}/reviews`, {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify(newReview)
            });
            if (!response.ok) {
                alert("حدث خطأ أثناء الإضافة.");
                return;
            }"""
    html = re.sub(add_old, add_new, html, flags=re.DOTALL)

    with open('admin.html', 'w', encoding='utf-8') as f:
        f.write(html)

if __name__ == '__main__':
    migrate()
    print("Done")
