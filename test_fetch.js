const { Client, Databases, Query } = require('node-appwrite');
const client = new Client()
    .setEndpoint('https://cloud.appwrite.io/v1')
    .setProject('6a36c593002500c98660');
const databases = new Databases(client);

databases.listDocuments('6a36cb6c0009fc808a1f', 'reviews', [Query.limit(5)])
    .then(res => console.log('Success. Found:', res.documents.length))
    .catch(err => console.error('Error:', err));
