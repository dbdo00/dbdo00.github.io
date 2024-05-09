const anchorTag =  document.getElementById("loginButton");
const outputToken = document.getElementById("output-token");
const outputEmail = document.getElementById("output-email");


anchorTag.addEventListener("click", (event) => {
    event.preventDefault();

    const authenticator = new netlify.configure({site_id: "94385d69-9efa-4e94-9d52-5c34b1afc240"});
    // netlify.configure({site_id: "94385d69-9efa-4e94-9d52-5c34b1afc240"});

    authenticator.authenticate(
        // Set the OAuth provider and token scope
        // Provider can be "github", "gitlab", or "bitbucket"
        // The scopes available depend on your OAuth provider
        { provider: "github", scope: "user" },
        async function (error, data) {
            if (error) {
                console.error(error);
            } else {
                const token = data.token;
                login();   
            }
        }
    );
});

