# Miro Blockchain Scout

Miro.com provides a simple SDK for developers to draw a connections chart. I dedided to utilize it in order to visualize on-chain connections for big crypto accounts. 

The first blockchain I implemented is Waves Protocol. You can see the result of script performance in the following diagram: [link](https://miro.com/app/board/uXjVMPtu_EE=/?share_link_id=106189705140).

<img width="1124" alt="image" src="https://user-images.githubusercontent.com/22869641/234046286-064c9905-31da-4fe5-a07a-b7b1c0695468.png">

## How To

To run this script you will need a Python 3.8+ and `requests` library pre-installed.

Also you will need to authorize as a Miro developer. It's pretty simple and takes maximum 3 minutes. To get your Bearer API token just follow the [Quickstart guideline](https://developers.miro.com/docs/rest-api-build-your-first-hello-world-app) or watch [this video](https://youtu.be/MEXNEy5HDSw).

As soon as you get Access Token, add it to the source file `wavesscout.py` and run it. After that, call `main(ADDRESS)` function, where `ADDRESS` is a Waves address (for example `3PC67eqTSZiXvnpLRo9odMAJ1EtXFKvKCJp`), whose connections you want to visualize. You will see some logs output and be able to find the chart in your Miro dashboard. 

## Outro

If you have successfully used this script, kindly add a star 🌟 to this repo. Appreciate it a lot!!!

Follow me in Twitter: https://twitter.com/vlzhr.
