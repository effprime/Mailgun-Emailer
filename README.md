# Mailgun Emailer
A Python library utilizing the Mailgun API

* Import the Module with `import mailgun_emailer`
* Start the emailer using your Mailgun URL and API key (see [Mailgun](https://documentation.mailgun.com/en/latest/api-intro.html#base-url))
  * `emailer = mailgun_emailer.MailgunEmailer(api_url="https://api.mailgun.net/v3", api_key="12345")`
  * You can provide the `api_url` and `api_key` in a separate `data.yaml` file
* Send an email using keyword arguments
  ```
  emailer.send_from_args(
    from="me@mysite.com",
    to="them@theirsite.com",
    subject="hello world",
    message="Dear World,\n\n Hello\n\n Me"
  )
  ```
* Send an email using a yaml file (see `send.example.yaml`)
  ```
  emailer.send_from_yaml("send.example")
  ```
