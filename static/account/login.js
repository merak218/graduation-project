var Main = {
    data () {
      return {
        openlogin: false,
        openregister: false,
        labelPosition: 'right',
        form: {
        username: '',
        password: '',
        account:''
      }
      };
    },
    methods: {
      openloginDialog () {
        this.openlogin = true;
      },
      closeloginDialog () {
        this.openlogin = false;
      },
      openregisterDialog () {
        this.openregister = true;
      },
      closeregisterDialog () {
        this.openregister = false;
      }
    }
  };
  var Ctor = Vue.extend(Main)
  new Ctor().$mount('#login')

  var ator = Vue.extend(Main)
  new ator().$mount('#register')