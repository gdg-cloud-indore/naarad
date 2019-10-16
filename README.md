# Naarad

The chivalrous messenger god is here to reduce your burden of Digital Publicity of your college events in facebook groups.

## Motivation

With every new event in college or any organisation, comes the burden of making it spread organically through facebook. A great way to do this is by posting it in multiple groups. It is a very tiresome and repetative task which can be excruciating at times.

## Features

- Allow posting in multiple groups by providing the list of groups and the required content.
- Accept list and content in multiple formats.
- Allow posting for two types of posts: embed and non embed.
- Allow posting a new post as well existing post.
- Create a installable pip package for the same.
- Secure and doesn't take password beyond user's system.

## Detailed Description

Below is a rough algorithm for the working of the application. This is to be improved as we move on with the project:

```text
Step: Take required input from the user
Step: Login to facebook with given credentials using web driver
Step: Selecting the type of post to be shared
Step: Open each link and using the web driver enter the form with data
Step: Post and show success message

The input taken will be:
- Phone Number / Email (for login)
- Password (for login)
- List of links (via batch file or entering manually)
- existing post or new post
- Text for the post
- Image / Link for the post
```

## Schedule

#### Phase I

Explore all the options and the tools required to accomplish the same. Get a knowledge of the DOM structure of Facebook.

#### Phase II

Create a basic structure for the project and implement the extracting and selection of DOM objects required for the process. Acceptance of input and formatting it should also be completed.

#### Phase III

Make it a pip package and finish up the coding phase. Write tests if time remains.

## Contribution Guidelines

Please raise a feature request or issue before sending PR for the same.

Follow the below guidelines for proper coding practices:

- Always [create a new branch](https://confluence.atlassian.com/bitbucket/branching-a-repository-223217999.html) for your changes and make PR from it ONLY.
- Write neat code with proper comments.
- Follow PEP8 coding style.
- Write descriptive commit messages. Please [read this](https://github.com/erlang/otp/wiki/writing-good-commit-messages) for more information.
- Write detailed PR messages and include `fixes #ISSUE_NUMBER` it if closes an issue, otherwise use `concerns #ISSUE_NUMBER` to tag the related issues. Please [refer here](https://github.blog/2015-01-21-how-to-write-the-perfect-pull-request/) for more PR guidelines.
- It is recommended to have a single commit for a task.
- Use [DRY principles](https://thealphadollar.github.io/learning/2019/05/13/go-dry.html) to create maintainable code.

## Communication
All contributors / users are requested to [Whatsapp](https://wa.me/919479756888) for further discussion on ideas, PRs and issues.

Mentor for the project: [Harshit Jain](https://www.github.com/iharshit009/).
