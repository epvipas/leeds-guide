from cats import add

# ---------------- SIGHTS ----------------
add("sights","Leeds Town Hall","The Headrow, LS1 3AD",
 "Cuthbert Brodrick's huge 1858 town hall, guarded by four stone lions, a symbol of Victorian Leeds' wool wealth.",
 "Your base for walking times",ta=True,geo="Leeds Town Hall")
add("sights","Kirkstall Abbey","Abbey Road, Kirkstall, LS5 3EH",
 "The best-preserved Cistercian abbey ruins in Britain, founded in 1152, in a riverside park. Free to wander, with a small visitor centre.",
 "Pair with Abbey House Museum across the road",far=True,geo="Kirkstall Abbey")
add("sights","Hyde Park Picture House","73 Brudenell Road, LS6 1JD",
 "A gem of an Edwardian cinema from 1914, still gas-lit, restored and showing independent and classic films.",
 "Check listings; pair with the Brudenell",far=True,geo="Hyde Park Picture House")
add("sights","Leeds Dock & the waterfront","Leeds Dock, LS10 1PZ",
 "Walk along the River Aire past converted warehouses to Leeds Dock and the Royal Armouries, with water taxis back to the station.",
 "Water taxi from Granary Wharf",ta=False,geo="Leeds Dock")

# ---------------- MUSEUMS ----------------
add("museums","Royal Armouries","Armouries Drive, LS10 1LT",
 "The national collection of arms and armour, from Henry VIII's armour to an elephant's battle armour, with live combat demonstrations. Free.",
 "Allow half a day; free entry",web="https://royalarmouries.org",geo="Royal Armouries Museum")
add("museums","Leeds City Museum","Millennium Square, LS2 8BH",
 "Free museum with the 3,000-year-old Egyptian mummy Nesyamun, the Leeds Tiger and a big floor map of the city.",
 "Free",web="https://museumsandgalleries.leeds.gov.uk",geo="Leeds City Museum")
add("museums","Thackray Museum of Medicine","141 Beckett Street, LS9 7LN",
 "A medical museum in an old workhouse, with a walk-through Victorian slum street and the history of surgery, gory and fascinating.",
 "Good with older children",geo="Thackray Museum of Medicine",ll=(53.8075,-1.5208))
add("museums","Leeds Industrial Museum, Armley Mills","Canal Road, Armley, LS12 2QF",
 "Once the largest woollen mill in the world, now a museum of Leeds manufacturing: textiles, printing, film and engineering, beside the canal.",
 "Walk or cycle the canal towpath to get there",far=True,geo="Leeds Industrial Museum")
add("museums","Abbey House Museum","Abbey Walk, Kirkstall, LS5 3EH",
 "A recreated Victorian street of shops and houses in the abbey's old gatehouse.",
 "Pair with Kirkstall Abbey",far=True,geo="Abbey House Museum")

# ---------------- GALLERIES ----------------
add("galleries","Leeds Art Gallery","The Headrow, LS1 3AA",
 "Free gallery with one of the best 20th-century British art collections outside London, including Henry Moore, Barbara Hepworth and Damien Hirst. The Tiled Hall café is stunning.",
 "Coffee in the Tiled Hall café",web="https://museumsandgalleries.leeds.gov.uk",geo="Leeds Art Gallery")
add("galleries","Henry Moore Institute","74 The Headrow, LS1 3AH",
 "One of Europe's most important sculpture galleries, with changing exhibitions and a research library, next to the Art Gallery. Free.",
 "Free · archive visits must be booked",geo="Henry Moore Institute")
add("bars","The Tetley","17–33 Hunslet Road, LS10 1JQ",
 "The art deco former headquarters of the Tetley brewery, which brewed in Leeds for nearly 200 years. The art centre that was here closed in 2023, and Kirkstall Brewery reopened the building in 2024 as a bar and restaurant.",
 "A short walk south of the river",price=2,geo="The Tetley, Leeds")

# ---------------- SHOPS & ARCADES ----------------
add("shops","Leeds Corn Exchange","Call Lane, LS1 7BR",
 "Cuthbert Brodrick's domed 1864 corn exchange, now full of independent shops: homeware, gifts, jewellery, vintage and design, around a breathtaking oval hall.",
 "Look up at the roof",geo="Leeds Corn Exchange")
add("shops","Victoria Quarter & County Arcade","Briggate, LS1 6BR",
 "Frank Matcham's ornate 1900 arcades of marble, mosaic and gold leaf, now home to designer shops, and Victoria Lane, covered with a huge stained-glass roof.",
 "The prettiest arcade in the north",geo="County Arcade, Leeds")
add("shops","Thornton's Arcade","Briggate, LS1 6LQ",
 "The city's first arcade, from 1878, with a clock of Ivanhoe characters that strike the hours. Independent shops including OK Comics, the Village Bookstore and Welcome Skate Store.",
 "Wait for the clock to strike",geo="Thornton's Arcade")
add("shops","Queens Arcade","Briggate, LS1 6LF",
 "An 1889 arcade linking Briggate to Lands Lane, with independent shops and a café gallery.",
 "Part of the arcades walk",geo="Queens Arcade, Leeds")
add("shops","Grand Arcade","New Briggate, LS1 6PG",
 "An 1897 arcade on New Briggate with a striking clock and a mix of independents, near the theatres.",
 "Pair with the Grand Theatre",geo="Grand Arcade, Leeds")

# ---------------- RECORDS, BOOKS & COMICS ----------------
add("records","Crash Records","35 The Headrow, LS1 6PU",
 "A Leeds institution for over 40 years: indie, alternative, rock, punk and metal on vinyl and CD, plus local gig tickets.",
 "Ask about local gigs",geo="Crash Records, Leeds",ll=(53.7998,-1.5425))
add("records","Jumbo Records","1–3 Merrion Centre, LS2 8NG",
 "The oldest record shop in Leeds, open since 1971, now in a bigger shop in the Merrion Centre, with every genre and big Record Store Day events.",
 "Huge on Record Store Day",geo="Jumbo Records, Leeds")
add("records","Tribe Records","28 Kirkgate, LS2 7DR",
 "A specialist shop for house, techno and dance vinyl, with DJ equipment.",
 "For dance-music diggers",ta=False,geo="Tribe Records, Kirkgate, Leeds",ll=(53.7962,-1.5388))
add("records","OK Comics","Thornton's Arcade, LS1 6LQ",
 "A much-loved independent comic and graphic novel shop in the Victorian arcade.",
 "Staff picks are excellent",ta=False,geo="OK Comics, Leeds",ll=(53.7983,-1.5420))
add("records","Colours May Vary","Leeds Corn Exchange, Call Lane, LS1 7BR",
 "An art and design bookshop and print shop on the top floor of the Corn Exchange.",
 "Great for prints and design books",ta=False,geo="Colours May Vary, Leeds",ll=(53.7965,-1.5410))

# ---------------- CAMERAS, MUSIC & TECH ----------------
add("gear","Northern Guitars","41 Call Lane, LS1 7BT",
 "Buying and selling new, used and vintage guitars, amps and pedals for over 25 years, upstairs from its own café-bar with live music.",
 "Try before you buy; coffee downstairs",ta=False,geo="Northern Guitars, Leeds")
add("gear","Hobgoblin Music","13 Eastgate, LS2 7LY",
 "A folk and acoustic instrument specialist with a second-hand section: mandolins, banjos, fiddles, whistles and guitars.",
 "Mon–Sat 10:00–18:00, Sun 11:00–16:00",ta=False,geo="Hobgoblin Music, Eastgate, Leeds")
add("gear","Wex Photo Video Leeds","Units F&G, Moor Allerton District Centre, LS17 5NY",
 "A big camera shop with a constantly changing second-hand counter, all with a 12-month warranty.",
 "Closed Sundays; check hours before going",far=True,geo="Wex Photo Video, Leeds")

# ---------------- VINTAGE ----------------
add("vintage","Blue Rinse","Silvercrest House, Call Lane, LS1",
 "Leeds' original vintage store: a five-storey flagship on Call Lane full of jackets, denim, sportswear and dresses. A smaller second shop is at 57 Merrion Street.",
 "The Merrion Street shop is near Jumbo Records",ta=False,who=["m","w"],geo="Blue Rinse Call Lane",ll=(53.7958,-1.5404))
add("vintage","Best Vintage","New Market Street, LS1 6DG",
 "One of the biggest vintage clothing shops in Leeds.",
 "Near Kirkgate Market",ta=False,who=["m","w"],geo="Best Vintage, Leeds",ll=(53.7968,-1.5398))
add("vintage","Ryan Vintage","13 Duncan Street, LS1 6DQ",
 "One of the longest-running and best-value vintage clothing shops in Leeds.",
 "Good for bargains",ta=False,who=["m","w"],geo="13 Duncan Street, Leeds",ll=(53.7963,-1.5418))

# ---------------- MARKETS & FOOD ----------------
add("markets","Kirkgate Market","Vicar Lane, LS2 7HY",
 "One of Europe's largest covered markets, in a magnificent 1904 hall. Marks & Spencer began here as a penny bazaar stall in 1884. Butchers, fishmongers, world food, street-food kitchens and record stalls.",
 "Saturday is busiest; record fairs some weekends",geo="Kirkgate Market")

# ---------------- CAFÉS ----------------
add("cafes","Laynes Espresso","16 New Station Street, LS1 5DL",
 "Ranked among the UK's best independent coffee shops in 2026, by the station, with excellent coffee and brunch.",
 "Expect a queue for brunch",price=1,geo="Laynes Espresso, Leeds",ll=(53.7956,-1.5462))
add("cafes","Miles & Co","Koncept Studios, 94 Kirkgate, LS2 7DJ",
 "A small specialty coffee spot that started in Kirkgate Market and now trades from Koncept Studios across the road.",
 "Coffee before or after the market",price=1,ta=False,geo="Miles & Co, Kirkgate, Leeds",ll=(53.7966,-1.5378))

# ---------------- EAT ----------------
add("mid","The Empire Cafe","6 Fish Street, LS1 6DB",
 "A 123-year-old former greasy spoon off Briggate, reinvented with seasonal small plates. Named Leeds' Best Restaurant at the 2026 Oliver Awards and 31st in the Good Food Guide's 100 best local restaurants for 2026.",
 "Book ahead now it's an award winner",price=2,geo="Empire Cafe, Leeds",ll=(53.7976,-1.5418))
add("mid","Ox Club","Headrow House, 19 The Headrow, LS1 6PU",
 "Live-fire cooking and a seasonal British menu, one of Leeds' most acclaimed independent restaurants.",
 "Check it's open: some listings show it closed",price=3,geo="Ox Club, Leeds",ll=(53.7996,-1.5422))
add("cheap","Bundobust","6 Mill Hill, LS1 5DQ",
 "Indian vegetarian street food and craft beer, the Leeds original of a now-famous group, winner of Best Street Food at the 2026 Oliver Awards.",
 "Order lots of small plates to share",price=1,geo="Bundobust, Mill Hill, Leeds")
add("mid","Tharavadu","7–8 Mill Hill, LS1 5DQ",
 "Keralan home cooking, repeatedly named Leeds' best Indian restaurant, with dosas, seafood curries and coconut everything.",
 "Book at weekends",price=2,geo="Tharavadu, Leeds")
add("mid","Shears Yard","11–15 Wharf Street, LS2 7EQ",
 "A modern European restaurant in an old rope-making warehouse in the Calls, regularly named among the city's finest independents.",
 "Good-value set menu",price=3,geo="Shears Yard, Leeds")

# ---------------- PUBS & BARS ----------------
add("pubs","Whitelocks","Turks Head Yard, off Briggate, LS1 6HB",
 "Leeds' oldest pub, from 1715, down a narrow yard off Briggate: a long bar of copper, brass and stained glass, named among the UK's best historic pubs and Leeds CAMRA's Winter 2024 Pub of the Season.",
 "Sit outside in the yard",price=1,geo="Whitelocks, Leeds")
add("pubs","The Angel Inn","Angel Inn Yard, off Briggate, LS1 6LN",
 "A historic Sam Smith's pub down another Briggate yard, with very cheap beer and lots of little rooms.",
 "Cash or card, but no music or phones",price=1,geo="Angel Inn, Leeds")
add("pubs","The Grove Inn","Back Row, Holbeck, LS11 5PL",
 "An unspoilt Victorian pub of small rooms, surrounded by tower blocks, with real ale and folk sessions.",
 "Near the station's south entrance",price=1,geo="Grove Inn, Holbeck, Leeds")
add("bars","North Bar","24 New Briggate, LS1 6NU",
 "Often called the UK's first craft-beer bar, opened in 1997, with a long, narrow room and a huge Belgian and craft list.",
 "Before or after the Grand Theatre",price=2,geo="North Bar, New Briggate, Leeds")
add("bars","Northern Monk Refectory","The Old Flax Store, Marshall Street, LS11 9YJ",
 "Northern Monk brewery's taproom in a listed mill building in Holbeck, with its own beers on tap.",
 "Close to the station's south side",price=2,geo="Northern Monk Refectory, Leeds")

# ---------------- MUSIC & THEATRE ----------------
add("music","Brudenell Social Club","33 Queen's Road, LS6 1NY",
 "A multi-award-winning 400-capacity venue in a working men's club in Hyde Park, often named one of the best small venues in Britain.",
 "Cheap bar; book gigs early",far=True,geo="Brudenell Social Club")
add("music","Belgrave Music Hall & Canteen","1–1a Cross Belgrave Street, LS2 8JP",
 "Three floors of bar, street food, a rooftop terrace and a 200-capacity gig space.",
 "The rooftop is great on a dry evening",geo="Belgrave Music Hall")
add("music","City Varieties Music Hall","Swan Street, LS1 6LW",
 "One of the oldest working music halls in the world, from 1865, home of TV's The Good Old Days, now hosting comedy, music and panto.",
 "Look up at the boxes",geo="City Varieties Music Hall",ll=(53.7987,-1.5428))
add("music","Leeds Grand Theatre","46 New Briggate, LS1 6NZ",
 "A grand Victorian theatre from 1878, home of Opera North and Northern Ballet, and the city's big panto.",
 "Pair with North Bar",geo="Leeds Grand Theatre")

# ---------------- THINGS TO DO ----------------
add("fun","Chance & Counters","Merrion Street, LS2",
 "A thriving board-game café open until midnight, with hundreds of games and staff to teach you.",
 "Book a table at weekends",geo="Chance and Counters, Leeds",ll=(53.8015,-1.5437))
add("fun","NQ64 Leeds","11 Merrion Street, LS1 6PQ",
 "A retro arcade bar with classic cabinets, pinball and game-themed cocktails.",
 "Free play in the day at weekends",geo="NQ64, Leeds",ll=(53.8014,-1.5442))
add("fun","Escape Hunt Leeds","The Light, The Headrow, LS1 8TL",
 "Themed escape rooms in The Light shopping centre on the Headrow.",
 "Book ahead",geo="Escape Hunt, Leeds",ll=(53.8005,-1.5468))

# ---------------- PARKS ----------------
add("parks","Roundhay Park","Princes Avenue, LS8 2ER",
 "One of the biggest city parks in Europe, 700 acres of lakes, woods and gardens, with the Tropical World glasshouses.",
 "Tropical World is great on a rainy day",far=True,drive="15 min",geo="Roundhay Park")
add("parks","Leeds & Liverpool Canal towpath","Granary Wharf, LS1 4BR",
 "Walk west from Granary Wharf along the canal past old mills to Armley Mills and on to Kirkstall Abbey, about 5 km.",
 "Bus back from Kirkstall",ta=False,geo="Granary Wharf, Leeds")

# ---------------- SPORT ----------------
add("sport","Headingley Stadium","St Michael's Lane, LS6 3BR",
 "Twin stadiums for Test cricket and Leeds Rhinos rugby league, where Botham's 1981 Ashes and Stokes's 2019 innings happened.",
 "Train to Headingley or bus from the centre",far=True,geo="Headingley Stadium")
add("sport","Elland Road (Leeds United)","Elland Road, LS11 0ES",
 "Home of Leeds United since 1919, with the Billy Bremner statue outside and stadium tours.",
 "Check tour dates around fixtures",far=True,geo="Elland Road Stadium")

# ---------------- DAY TRIPS ----------------
add("trips","Harewood House","Harewood, LS17 9LG",
 "A grand Georgian house with Chippendale furniture, Capability Brown grounds, a bird garden and Christmas displays.",
 "Christmas season runs into January",far=True,drive="25 min",geo="Harewood House")
add("trips","Saltaire & Salts Mill","Victoria Road, Saltaire, BD18 3LA",
 "A UNESCO World Heritage model village built by Titus Salt for his mill workers. Salts Mill now has a big David Hockney gallery, books and a diner.",
 "Free Hockney gallery; combine with a canal walk",far=True,drive="25 min",geo="Salts Mill")
add("trips","The Hepworth Wakefield","Gallery Walk, Wakefield, WF1 5AW",
 "A striking riverside gallery devoted to Barbara Hepworth and modern British art, with a lovely garden.",
 "Free; pair with Yorkshire Sculpture Park",far=True,drive="25 min",geo="The Hepworth Wakefield")
add("trips","Haworth & the Brontë Parsonage","Church Street, Haworth, BD22 8DR",
 "The cobbled moorland village where the Brontë sisters wrote, with their home as a museum, and the Keighley & Worth Valley steam railway below.",
 "Walk up onto the moors to Top Withens",far=True,drive="45 min",geo="Brontë Parsonage Museum")
add("trips","Ilkley & the Cow and Calf","Ilkley, LS29 8BT",
 "A Victorian spa town with independent shops and Bettys tea rooms, below Ilkley Moor's famous Cow and Calf rocks.",
 "Walk up to the rocks for the view",far=True,drive="35 min",geo="Cow and Calf Rocks",ll=(53.9168,-1.8037))
add("trips","York","York Minster, YO1 7HH",
 "A walled medieval city with York Minster, the Shambles and the National Railway Museum.",
 "Train is easier than parking: 25 minutes",far=True,drive="45 min",geo="York Minster")

# ---------------- REVIEW ADDITIONS (Nov 2026) ----------------
add("cafes","Kapow Coffee (Thornton's Arcade)","15 Thornton's Arcade, LS1 6LQ",
 "Speciality coffee over three floors, up a steep staircase, in the Victorian arcade. The original branch is at 46 The Calls.",
 "Head upstairs for a quieter seat",price=1,geo="Kapow Coffee, Thornton's Arcade")
add("cafes","La Bottega Milanese","2 Bond Court, LS1 2JZ",
 "A long-running Italian-style espresso bar (its branch in The Light closed in 2020) with proper cornetti, one of Leeds' best-regarded independents.",
 "Stand at the bar for a quick espresso, Milan-style · check it's open",price=1,geo="La Bottega Milanese, Bond Court, Leeds",ll=(53.7975,-1.5495))
add("cheap","Amazing Gyoza","Kirkgate Market, Vicar Lane, LS2 7HY",
 "A market stall making hand-folded dumplings, fried or steamed, for a few pounds: one of the market's best-value lunches.",
 "Go before 1pm on Saturdays to avoid the queue",price=1,ta=False,geo="Kirkgate Market",ll=(53.7971,-1.5392))
add("cheap","Trinity Kitchen","Trinity Leeds, Albion Street, LS1 5AT",
 "A street-food hall inside the Trinity shopping centre, with permanent stalls plus guest traders that change regularly.",
 "Quick, easy lunch while shopping",price=1,geo="Trinity Kitchen, Leeds")
add("splurge","Chef Jono at V&V","68 New Briggate, LS1 6NU",
 "A small fine-dining restaurant with inventive modern British tasting menus. On Sundays it serves a five-course roast-dinner tasting menu.",
 "Wed–Sat evenings and Sunday lunch; book ahead",price=4,geo="Chef Jono at V&V, Leeds")
add("mid","Kendells Bistro","3 St Peter's Square, LS9 8AH",
 "A long-running candlelit French bistro serving classics such as steak frites and moules from a chalkboard menu.",
 "Tue–Sat from 17:30 · early-evening set menu is good value",price=3,geo="Kendells Bistro, Leeds")
add("bars","Tabula Rasa","8 Eastgate, LS2 7JL",
 "An art deco aperitivo and cocktail bar behind Victoria Gate, named in the 2026 UK Top 50 Cocktail Bars. Café by day, cocktails by night.",
 "Closed Mondays",price=3,geo="Tabula Rasa, Eastgate, Leeds")
add("bars","Water Lane Boathouse","Canal Wharf, Water Lane, LS11 5PS",
 "A canalside bar and kitchen at Granary Wharf with a big terrace over the water and a shelf of board games.",
 "Best on a sunny afternoon",price=2,geo="Water Lane Boathouse")
add("pubs","Victoria Family & Commercial","28 Great George Street, LS1 3DL",
 "An ornate 1865 pub right behind the Town Hall, with etched glass, carved wood and snugs. It reopened in December 2025 under Kirkstall Brewery and Whitelock's after more than five years closed.",
 "Two minutes from the Town Hall",price=2,geo="Victoria Family and Commercial, Leeds")
add("pubs","The Duck & Drake","43 Kirkgate, LS2 7DR",
 "An unpretentious old boozer by Kirkgate Market with a long list of real ales and regular blues and rock gigs.",
 "Live music most weekends",price=1,geo="Duck and Drake, Leeds")
add("music","Headrow House","19 The Headrow, LS1 6PU",
 "A multi-floor venue in a former textile mill, with a beer hall, roof terrace and a small upstairs room for gigs and DJs. Ox Club is inside.",
 "Check gig listings; the roof terrace is free to visit",geo="Headrow House, Leeds")
add("music","Hyde Park Book Club","27–29 Headingley Lane, LS6 1BL",
 "A café-bar by day and a small basement venue by night, hosting indie gigs, comedy and spoken word.",
 "Pair with the Hyde Park Picture House",far=True,geo="Hyde Park Book Club")
add("food","George & Joseph Cheesemongers","140 Harrogate Road, Chapel Allerton, LS7 4NZ",
 "An award-winning cheesemonger, strong on British farmhouse cheeses with tastings at the counter.",
 "Combine with Chapel Allerton's cafés and bars",far=True,geo="George & Joseph Cheesemongers")
add("food","The Cheesy Living Co","Leeds Corn Exchange, Call Lane, LS1 7BR",
 "A cheese and charcuterie deli inside the Corn Exchange, also serving grazing boards to eat in.",
 "Good place to pick up a picnic or a gift",ta=False,geo="Corn Exchange, Leeds",ll=(53.7962,-1.5412))
add("vintage","Shush Interiors","Leeds Corn Exchange, Call Lane, LS1 7BR",
 "Retro and mid-century furniture, lighting and one-off homewares, now in the Corn Exchange.",
 "Stock changes weekly; ask about delivery for big pieces",ta=False,geo="Corn Exchange, Leeds",ll=(53.7964,-1.5409))
add("charity","BHF Furniture & Electrical, Colton","Unit 4, Colton Retail Park, LS15 9JB",
 "A large British Heart Foundation superstore selling second-hand sofas, tables, beds, wardrobes and tested electrical appliances.",
 "Mon–Sat 9:00–18:00, Sun 10:30–16:30; bring a car for big buys",far=True,drive="15 min",geo="Colton Retail Park")
add("galleries","The Gallery at 164","Café 164, Munro House, Duke Street, LS9 8AG",
 "An independent gallery inside Café 164 near Quarry Hill, with changing shows by established and emerging artists, free to browse, with work for sale.",
 "Check the website for current exhibitions",geo="Munro House, Leeds",ll=(53.7985,-1.5340))
add("galleries","Craft Leeds","Leeds Art Gallery (lower level), The Headrow, LS1 3AB",
 "A retail gallery of contemporary craft and design (ceramics, jewellery, glass and prints) by UK makers, trading since 1982.",
 "Good for gifts made by makers",ta=False,geo="Leeds Art Gallery",ll=(53.8002,-1.5482))
add("galleries","Sunny Bank Mills","Town Street, Farsley, LS28 5UJ",
 "A restored worsted mill with a contemporary gallery, the mill archive, independent shops and a café, plus a gig and comedy venue.",
 "Free gallery; check what's on",far=True,drive="20 min",geo="Sunny Bank Mills")
add("fashion","Flannels (Briggate flagship)","115–126 Briggate, LS1 6EY",
 "A six-floor luxury fashion flagship in the former Debenhams building, opened in October 2024, stocking designer brands for men, women and children.",
 "One of the biggest designer stores outside London",who=["m","w","k"],geo="Flannels, Briggate, Leeds",ll=(53.7985,-1.5426))
add("parks","Temple Newsam","Temple Newsam Road, LS15 0AE",
 "A Tudor-Jacobean house in 1,500 acres of Capability Brown parkland, with Home Farm, a rare-breeds working farm. The park is free to walk.",
 "Allow half a day; parking is paid",far=True,drive="15 min",web="https://museumsandgalleries.leeds.gov.uk",geo="Temple Newsam House")
add("parks","Golden Acre Park","Otley Road, Bramhope, LS16 9JY",
 "A free park around a lake with gardens and woodland, the starting point for walks out to the Chevin and Eccup.",
 "Café on site",far=True,drive="20 min",geo="Golden Acre Park")
add("parks","Meanwood Valley Trail","Meanwood Park, Green Road, LS6 4LZ",
 "A seven-mile waymarked walk from Woodhouse Ridge through Meanwood Park and the woods to Golden Acre Park, following a beck past old mill ponds.",
 "Do the Meanwood Park to Adel section if short of time",far=True,geo="Meanwood Park")
add("trips","Yorkshire Sculpture Park","West Bretton, Wakefield, WF4 4LG",
 "500 acres of parkland with open-air works by Henry Moore, Barbara Hepworth and many others, plus indoor galleries.",
 "Wear walking shoes; parking is paid",far=True,drive="30 min",web="https://ysp.org.uk",geo="Yorkshire Sculpture Park")
add("trips","Hebden Bridge","Hebden Bridge, HX7 8AD",
 "A former mill town in a steep Pennine valley, full of independent shops, cafés and canal walks, with a walk up to Hardcastle Crags.",
 "The train from Leeds takes about 50 minutes",far=True,drive="45 min",geo="Hebden Bridge")
add("trips","Knaresborough","Knaresborough, HG5 8AE",
 "A market town with a railway viaduct over the River Nidd, castle ruins, rowing boats and Mother Shipton's Cave.",
 "Wednesday is market day",far=True,drive="35 min",geo="Knaresborough Castle")
add("trips","Otley","Otley, LS21 3AE",
 "A market town below the Chevin, with Friday and Saturday markets, old pubs and a climb up to Surprise View.",
 "Go on a market day; walk up the Chevin",far=True,drive="30 min",geo="Otley Market Place")
