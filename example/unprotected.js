var UnProtectedPage = {
  template : `
<div style="margin:20px;">
  <h1>Hello Unprotected World!</h1>
  <p>
    Just a few manual steps and you're good to go.<br>
    Visit <a href="https://console.cloud.google.com">https://console.cloud.google.com</a> and ...
  </p>

  <h2>Create a new project...</h2>
  <p>
    <img src="/app/static/images/google-create-project.png" width="800">
  </p>

  <h2>Set up a consent page...</h2>
  <p>
    <img src="/app/static/images/google-consent-page.png" width="800">
  </p>

  <h2>Create API credentials...</h2>
  <p>
    <img src="/app/static/images/google-credentials.png" width="800">
  </p>

  </p>
</div>
`,
  navigation: {
    icon:    "lock_open",
    text:    "Unprotected",
    path:    "/",
    index:   1
  }
};

Navigation.add(UnProtectedPage);
