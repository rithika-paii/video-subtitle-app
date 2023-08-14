<template>
    <div class="video-upload">
        <div class="header">
            <h2 class="title">Video Subtitle Editor</h2>
        </div>
        <div class="uploader-container">
            <input type="file" @change="handleFileChange" accept="video/*">
            <video ref="videoPlayer" controls></video>
            <textarea class="subtitle-input" v-model="subtitleText" placeholder="Add subtitle"></textarea>
            <button class="add-subtitle-btn" @click="addSubtitle">Add Subtitle</button>
            <button class="auto-subtitle-btn" @click="generateAutoSubtitles">Auto-Subtitle</button>
          </div>
    </div>
  </template>
  
  <script>
  import axios from 'axios';

  export default {
    data() {
      return {
      videoId: null,             // Initialize with null
      subtitleText: "",
      yourSubtitlesArray: [],
      };
    },
    methods: {
      handleFileChange(event) {
        this.videoFile = event.target.files[0];
        this.$refs.videoPlayer.src = URL.createObjectURL(this.videoFile);
      },
      async addSubtitle() {
        const currentTime = this.$refs.videoPlayer.currentTime;
        this.$emit("add-subtitle", currentTime, this.subtitleText);
        this.subtitleText = "";

        try {
        const response = await axios.post('http://localhost:5000/create_subtitles', {
          video_id: this.videoId,                // Use the video ID from data
          subtitles: this.yourSubtitlesArray,    // Use the subtitles array from data
        });
        console.log(response.data.message);
        } catch (error) {
        console.error('Error creating subtitles:', error);
        }
      },
    },
  };
  </script>
  
<style scoped>
 .video-upload {
  text-align: center;
  padding: 20px;
  background-color: #f9f9f9;
  border-radius: 10px;
}
.header {
  background-color: #007bff;
  color: white;
  padding: 10px 0;
  border-top-left-radius: 10px;
  border-top-right-radius: 10px;
}
.title {
  font-size: 24px;
  margin: 0px;
}

.uploader-container {
  display: flex;
  flex-direction: column;
  align-items: center;
  margin-top: 20px;
}

.subtitle-input {
  width: 100%;
  height: 60px;
  padding: 10px;
  margin: 10px 0;
  border: 1px solid #ccc;
  border-radius: 5px;
  font-size: 14px;
}

.add-subtitle-btn {
  background-color: #007bff;
  color: white;
  border: none;
  padding: 10px 20px;
  border-radius: 5px;
  cursor: pointer;
  font-size: 16px;
  transition: background-color 0.3s;
}

.add-subtitle-btn:hover {
  background-color: #0056b3;
}
</style>