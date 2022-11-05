import { upload } from 'youtube-videos-uploader' //Typescript
//OR
const { upload } = require('youtube-videos-uploader'); //vanilla javascript

// recoveryemail is optional, only required to bypass login with recovery email if prompted for confirmation
const credentials = { email: 'Your Email', pass: 'Your Password', recoveryemail: 'Your Recovery Email' }

// minimum required options to upload video
const video1 = { path: '1.mp4', title: 'title 1', description: 'description 1' }

const onVideoUploadSuccess = (videoUrl) => {
    // ..do something..
}
// Extra options like tags, thumbnail, language, playlist etc
const video2 = { path: 'video2.mp4', title: 'title 2', description: 'description 2', thumbnail:'thumbnail.png', language: 'english', tags: ['video', 'github'], playlist: 'playlist name', channelName: 'Channel Name', onSuccess:onVideoUploadSuccess, skipProcessingWait: true, onProgress: (progress) => { console.log('progress', progress) } }


// Returns uploaded video links in array
upload (credentials, [video1, video2]).then(console.log)

// OR
// This package uses Puppeteer, you can also pass Puppeteer launch configuration
upload (credentials, [video1, video2], {headless:false}).then(console.log)

// Refer Puppeteer documentation for more launch configurations like proxy etc
// https://pptr.dev/#?product=Puppeteer&version=main&show=api-puppeteerlaunchoptions