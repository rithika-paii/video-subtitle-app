<template>
  <div id="app">
    <VideoUpload @add-subtitle="addSubtitle" />
    <Subtitles :subtitles="subtitles" @update-current-subtitle="setCurrentSubtitle" />
  </div>
</template>

<script>
import VideoUpload from "./components/VideoUpload.vue";
import Subtitles from "./components/AudioFile.vue";

export default {
  components: {
    VideoUpload,
    Subtitles,
  },
  data() {
    return {
      subtitles: [],
      currentSubtitle: null,
    };
  },
  methods: {
    addSubtitle(time, text) {
      this.subtitles.push({ time, text });
    },
    setCurrentSubtitle(subtitle) {
      this.currentSubtitle = subtitle;
    },
  },
};
</script>
