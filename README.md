<h1> Polybar-Stonks </h1>

This is a polybar module that tracks cryptocurrency prices using the CoinMarketCap API. Unlike other modules that use their old API and no longer work, this is written from the ground-up to utilize the API in its current form. You'll need to get a (free) API key, which you can find [here](https://coinmarketcap.com/api). Append your API key into `stonks-config.ini`.

You can track any cryptocurrency supported by the API - this includes BTC, ETC, XRP, etc. Just edit stonks-config.ini as needed. Additionally, you can track percent change over the last hour, day, or week.

Currently, I'm not including icons in the module. I use bitmap fonts on my own polybar configuration and there are no good bitmap icon fonts for cryptocurrency symbols. If there's enough demand, I'll try to include them. 

The module updates every 300 seconds by default. This is due to API limitations - you can only call it 333 times a day, so hypothetically you could call it once every 259 seconds, or more if you don't have it running 24 hours a day. If you're in a position where you need more frequent updates, you have to upgrade your plan with them.

<h2>Installation</h2>

```
git clone https://github.com/dreamsmasher/polybar-stonks.git ~/.config/polybar/stonks
cd ~/.config/polybar/stonks
./install.sh
```

Now, just add `stonks` to your `config.ini`. Enjoy!



