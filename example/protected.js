var AProtectedPage = {
  template : `
<ProtectedPage bannerImage="/app/static/images/locked.png">

  <template v-slot:login>
    <h3 class="headline mb-0">✋ To access this page,...</h3>
    <p>

      Hi there. Welcome to <i>this example</i>. If you have followed the
      instructions on the unprotected page, you now can proceed below and log
      in using your Google account.

    </p>  
  </template>

  <h1>Hello Protected World!</h1>

  <p>
    TODO: explain what just happened... page -> google -> session
  </p>

</ProtectedPage>
`,
  navigation: {
    icon:    "lock",
    text:    "Potected",
    path:    "/protected",
    index:   2
  }
};

Navigation.add(AProtectedPage);
