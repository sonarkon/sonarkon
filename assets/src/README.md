Card generator for the profile README (800×400, rendered at 2× = 1600×800).

    npm i @fontsource/fraunces@5.1.0 @fontsource/inter@5.1.0 playwright
    python3 gen.py                                   # writes <name>.html per card
    node render.js hope-tv.html hope-tv.png 800 400 2      # card
    node render.js hope-tv.html hope-tv-social.png 800 400 1.6   # 1280×640 social preview

Cards made from existing art:
- Common Shrew and Dome-Sim use those repos' social-preview images, downscaled.
- Kerf-O-Matic 9000 combines readme-banner.png with a strip of kerf-o-matic-2d.jpg.
- `moon.jpg` comes from HOPE-TV (hopetv/data/05_mond_3.jpg).
