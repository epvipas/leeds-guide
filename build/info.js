// ---------- info ----------
function iref(id, label) { const it = ITEMS.find(x => x.id === id); return `<button class="linkchip" data-goto="${id}" style="color:${CATS[it.cat].color}">${CATS[it.cat].emoji} ${esc(label || it.name)}</button>`; }
function byName(n) { const it = ITEMS.find(x => x.name === n); if (!it) throw new Error('No place called ' + n); return it.id; }
function refs(names) { return names.map(n => iref(byName(n))).join(' '); }
function renderSpecial() {
  const stops = [
    ['Leeds Corn Exchange', 'Start under Brodrick\'s great oval dome, full of independents.'],
    ['Kirkgate Market', 'Cross Vicar Lane to the 1904 market hall, where M&S began.'],
    ['Victoria Quarter & County Arcade', 'Frank Matcham\'s marble and gold arcades and the stained-glass roof of Victoria Lane.'],
    ['Whitelocks', 'Duck down Turks Head Yard to the city\'s oldest pub, from 1715.'],
    ['Thornton\'s Arcade', 'Cross Briggate for the 1878 arcade and its Ivanhoe clock.'],
    ['Queens Arcade', 'Next door, through to Lands Lane.'],
    ['The Angel Inn', 'Another Briggate yard pub.'],
    ['Grand Arcade', 'Finish up on New Briggate by the Grand Theatre.'],
    ['North Bar', 'A drink at what\'s often called the UK\'s first craft-beer bar.'],
  ];
  $('#specialTrail').innerHTML = '<ol>' + stops.map(([n, t]) => `<li style="margin-bottom:8px">${iref(byName(n))}<br>${esc(t)}</li>`).join('') + '</ol>';
}
function renderInfo() {
  const hq = { q: 'Leeds Town Hall, The Headrow, Leeds', name: 'Leeds Town Hall', ta: true };
  $('#v-info').innerHTML = `
  <div class="hero"><img src="img/cover.svg" alt=""><div class="cap"><span style="color:#FFD23F;font-size:11px;font-weight:800;letter-spacing:2px">YOUR BASE</span><br><b>Leeds Town Hall</b><br><span style="font-size:13px">The Victorian town hall with four stone lions on the Headrow. Walking times in the guide are from here.</span></div></div>
  <div class="sec"><h2>🚗 Getting there</h2>
   <img src="img/transit.svg" alt="" style="width:100%;border-radius:12px;aspect-ratio:16/7;object-fit:cover">
   <div class="opt" style="border-color:#1F4E46"><h4 style="background:#1F4E46"><span>🚌 Park &amp; Ride</span><span>easy from the M1 and A64</span></h4><ol>
    <li>Leeds has Park &amp; Ride sites at <b>Elland Road</b> (M621 J2), <b>Temple Green</b> (M1 J45) and <b>Stourton</b>, with buses into the centre. Check fares and times before you go.</li></ol></div>
   <div class="opt" style="border-color:#D4A03A"><h4 style="background:#D4A03A"><span>🅿️ Driving in</span><span>multi-storeys</span></h4><ol>
    <li>Central car parks include <b>Victoria Gate</b> (for the arcades and market), <b>Trinity</b> and the <b>Merrion Centre</b>.</li></ol></div>
   <div class="opt" style="border-color:#1877D0"><h4 style="background:#1877D0"><span>🚆 By train</span><span>10 min walk</span></h4><ol>
    <li>Leeds station is a short walk south of Briggate and the arcades. Laynes Espresso is right outside.</li></ol></div>
   ${actions(hq, true)}
  </div>
  <div class="sec"><h2>🗓️ Two easy days</h2>
   <div class="day" style="background:#FDE3DF"><b>Day 1 · Arcades, market &amp; records:</b> ${refs(['Laynes Espresso', 'Leeds Corn Exchange', 'Kirkgate Market', 'Victoria Quarter & County Arcade', 'Thornton\'s Arcade', 'Crash Records', 'Jumbo Records', 'Whitelocks', 'The Empire Cafe'])}</div>
   <div class="day" style="background:#DDEBFA"><b>Day 2 · Art, armour &amp; the river:</b> ${refs(['Leeds Art Gallery', 'Henry Moore Institute', 'Leeds City Museum', 'Bundobust', 'Leeds Dock & the waterfront', 'Royal Armouries', 'Northern Monk Refectory', 'Brudenell Social Club'])}</div>
  </div>
  <div class="sec"><h2>🔎 Second-hand hunting</h2>
   <div class="day" style="background:#FDEFD6"><b>Cameras, guitars, records &amp; vintage:</b> ${refs(['Northern Guitars', 'Hobgoblin Music', 'Wex Photo Video Leeds', 'Tribe Records', 'Blue Rinse', 'Best Vintage', 'Ryan Vintage'])}
    <p style="margin:8px 0 0;font-size:13px">Northern Guitars and Blue Rinse are both on Call Lane. West Yorkshire Cameras' shop has closed.</p></div>
  </div>
  <div class="sec"><h2>🎸 Nights out &amp; sport</h2>
   <div class="day" style="background:#EFE2F8"><b>Gigs, theatre &amp; games:</b> ${refs(['Brudenell Social Club', 'Belgrave Music Hall & Canteen', 'City Varieties Music Hall', 'Leeds Grand Theatre', 'Hyde Park Picture House', 'Chance & Counters', 'NQ64 Leeds'])}</div>
   <div class="day" style="background:#D8F3EE"><b>Sport:</b> ${refs(['Headingley Stadium', 'Elland Road (Leeds United)'])}</div>
  </div>
  <div class="sec"><h2>🚗 Day trips</h2>
   <div class="day" style="background:#D8F3EE"><b>Art &amp; heritage:</b> ${refs(['Saltaire & Salts Mill', 'The Hepworth Wakefield', 'Harewood House', 'Kirkstall Abbey'])}</div>
   <div class="day" style="background:#FDE3DF"><b>Moors &amp; old cities:</b> ${refs(['Haworth & the Brontë Parsonage', 'Ilkley & the Cow and Calf', 'York'])}</div>
  </div>
  <div class="sec"><h2>🕐 Opening hours</h2><ul>
   <li>Kirkgate Market is busiest on Saturdays and closed on Sundays.</li>
   <li>The city's council museums and galleries are free, and several close on Mondays.</li>
   <li>Book weekend dinners ahead, especially award winners like the Empire Cafe.</li></ul></div>
  <div class="sec"><h2>⚠️ Before you go</h2><ul>
   <li><b>Recently closed:</b> Tapped, Salvio's, Emba, Revolution Electric Press, Geek Retreat Leeds and West Yorkshire Cameras' shop have all closed, and The Tetley art centre is now a bar, so they're not in the guide.</li>
   <li>Independent places change often. Check each venue's own site or socials before a special trip.</li>
   <li>Map pins come from OpenStreetMap and are close but not exact; use the Directions buttons for door-to-door routes.</li>
   <li>Information was checked in November 2026. The illustrations are original artwork drawn for this guide.</li></ul>
   <button class="btn b-map" id="installAgain" style="width:100%;margin-top:8px">📲 Install this guide on your phone</button></div>
  <div class="sec"><h2>🔄 Updates</h2><p>The guide checks for new content whenever you're online. If something looks out of date, tap below to clear the saved copy and reload.</p>
  <button class="iconbtn" id="refreshBtn" style="padding:10px 14px;box-shadow:0 1px 5px rgba(0,0,0,.2)">Refresh guide</button></div>`;
}
