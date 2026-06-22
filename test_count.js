const sdk = require('appwrite');
const client = new sdk.Client()
    .setEndpoint('https://fra.cloud.appwrite.io/v1')
    .setProject('6a36c593002500c98660');
const databases = new sdk.Databases(client);
async function run() {
    const res = await databases.listDocuments('6a36cb6c0009fc808a1f', 'reviews', [sdk.Query.limit(500)]);
    const haraj = res.documents.filter(r => r.isHaraj !== false);
    console.log("Total Haraj reviews: ", haraj.length);
}
run();
