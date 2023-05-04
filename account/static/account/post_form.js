let data = {
    labelPosition: 'right',
    options: [
      '版型一', '版型二', '版型三',
      '版型四', '版型五', '客製化'
    ],
    post_form: {
      title: '',
      date_post: '',
      edition:'',
      video_url: '',
      mar_text: '',
      image: '',
      content:'',
      qrcode: ''
    }
  }
  
  
  let vm = new Vue({
    el: '#post_form',
    delimiters:['${', '}'],
    data : data
  })