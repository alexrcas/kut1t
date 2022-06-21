const { createApp } = Vue


createApp({

compilerOptions: {
    delimiters: ["[[", "]]"]
    },


  data() {
    return {
      url: '',
      shortUrl: '',
      buttonEnabled: true,
      textareaDisabled: false,
      isWaiting: false,
      error: false,
      kuts: []
    }
  },


  methods: {

    async short() {
        this.buttonEnabled = false;
        this.textareaDisabled = true;
        this.isWaiting = true;
        this.error = false;
        const response = await fetch('/short', {
            method: 'POST',
            headers: {
                'Accept': 'application/json',
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                url: this.url
            })
        })

        if (response.status >= 400) {
          this.error = true;
          this.shortUrl = null
        } else {
          const data = await response.json()
          this.shortUrl = data.url
          this.save(data)
          this.kuts = this.load()
        }

        this.textareaDisabled = false;
        this.isWaiting = false;
    },

    copyToClipboard() {
      navigator.clipboard.writeText(this.shortUrl);
      const notification = new Notyf({
        position: {
          x: 'center',
          y: 'bottom'
        }
      });
      notification.success('Copied to Clipboard!')
    },

    enableButton() {
      this.buttonEnabled = true;
    },

    save(kut) {
      const data = window.localStorage.getItem('kuts');
      const kuts = data ? JSON.parse(data) : []

      if (kuts.length > 4) {
        kuts.pop()
      }
      window.localStorage.setItem('kuts', JSON.stringify([kut, ...kuts]))
    },

    load() {
      const data = window.localStorage.getItem('kuts');
      return data ? JSON.parse(data) : []
    }

  },

  mounted() {
    this.kuts = this.load();
  }


}).mount('#app')