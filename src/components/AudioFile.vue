<template>
    <div class="subtitles-container">
      <video ref="videoPlayer" controls @timeupdate="updateSubtitle"></video>
      <div class= "subtitle-box" v-for="subtitle in subtitles" :key="subtitle.time">
        <p>{{ subtitle.text }}</p>
      </div>
    </div>
  </template>
  
  <script>

  import axios from 'axios';
  export default {
    data() {
      return {
        videoId: 'your_video_id',      // Replace with the actual video ID
        yourSubtitlesArray: [],        // Initialize as an empty array
        currentSubtitle: null,
      };
    },
    methods: {
      async updateSubtitle() {
        const currentTime = this.$refs.videoPlayer.currentTime;
        const currentSubtitle = this.subtitles.find(subtitle => subtitle.time <= currentTime);
        this.$emit("update-current-subtitle", currentSubtitle);

        try {
        const response = await axios.get(`http://localhost:5000/get_subtitles/${this.videoId}`);
        this.yourSubtitlesArray = response.data;  // Update subtitles array
        // Update your subtitles in the component
        } catch (error) {
        console.error('Error getting subtitles:', error);
        }
      },
    },
  };
  </script>
  
  <style scoped>
  .subtitles-container {
    text-align: center;
    padding: 20px;
  }
  
  .subtitle-box {
    background-color: rgba(0, 0, 0, 0.7);
    color: white;
    padding: 10px;
    margin: 10px 0;
    border-radius: 5px;
    font-size: 14px;
  }
  </style>