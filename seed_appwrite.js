const fs = require('fs');

const PROJECT_ID = '6a36c593002500c98660';
const DATABASE_ID = '6a36cb6c0009fc808a1f';
const COLLECTION_ID = 'reviews';
const ENDPOINT = `https://cloud.appwrite.io/v1/databases/${DATABASE_ID}/collections/${COLLECTION_ID}/documents`;

async function seed() {
    console.log('Reading extracted_reviews.json...');
    const raw = fs.readFileSync('extracted_reviews.json', 'utf8');
    const reviews = JSON.parse(raw);

    // Upload in reverse order so the newest (top of json) gets created last, 
    // or upload in order but appwrite handles sorting by $createdAt.
    // If we upload in reverse order, the newest ones will have a newer $createdAt.
    console.log(`Found ${reviews.length} reviews to upload...`);

    // Let's reverse the array so the oldest is uploaded first
    reviews.reverse();

    // Start from 180 since the previous run uploaded the first 180 before rate limit
    let startIndex = 180;
    
    for (let i = startIndex; i < reviews.length; i++) {
        const r = reviews[i];
        try {
            const res = await fetch(ENDPOINT, {
                method: 'POST',
                headers: {
                    'X-Appwrite-Project': PROJECT_ID,
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({
                    documentId: 'unique()',
                    data: {
                        name: r.name ? r.name.substring(0, 255) : "مجهول",
                        date: r.date || "",
                        text: r.text || "",
                        isHaraj: true
                    }
                })
            });

            if (!res.ok) {
                if (res.status === 429) {
                    console.log("Rate limit hit! Waiting 60 seconds...");
                    await new Promise(resolve => setTimeout(resolve, 60000));
                    i--; // retry this review
                    continue;
                }
                const text = await res.text();
                console.error(`Failed to upload review ${i + 1}: ${text}`);
                if (res.status === 401 || res.status === 403) {
                    console.error("PERMISSION ERROR");
                    break;
                }
            } else {
                if (i % 10 === 0) {
                    console.log(`Uploaded review ${i + 1}/${reviews.length}`);
                }
            }
            
            await new Promise(resolve => setTimeout(resolve, 500));
        } catch (e) {
            console.error(`Error on review ${i + 1}:`, e);
            await new Promise(resolve => setTimeout(resolve, 5000));
        }
    }
    
    console.log('Finished uploading reviews!');
}

seed();
