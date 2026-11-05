# HyperFrames handoff prompt

Paste everything below the line into Claude Code (with the HyperFrames skills installed: `npx skills add heygen-com/hyperframes`).

---

Using the HyperFrames skills, build and render a main 16:9 1920x1080 stickman psychology video, about 10:00 long, 30fps. Title: "तुमचं मूल नवीन मुलांमध्ये का मिसळत नाही?" Language: Marathi (Devanagari).

Voiceover: if I give you a recorded file at assets/vo.wav, use it. Otherwise generate it with /hyperframes-media TTS from the script at the end, but first confirm the TTS voice supports Marathi and play me one test paragraph before generating the full track. If it doesn't support Marathi, stop and tell me. Use the final audio's timing to drive scene timing and word-by-word captions (transcribe with Marathi language set, or force-align to the script). Scene times in the table are targets: stretch or shrink scenes to match the real audio.

Draw every character and prop with SVG shapes as described. Use no external images. Never draw real researchers: researcher cards are text only. Load the Mukta font from Google Fonts for all Devanagari text.

## 1. Style

- Clean off-white background `#FAF7F2`. Black stickman lines `#1A1A1A`, about 6px thick at 1080p, with rounded caps and joints.
- Round heads with expressive eyes and eyebrows. The expressions carry the emotion.
- 1 or 2 flat props per scene, drawn with simple shapes. No external images.
- **Accent colour:** amber `#F08C00`, used for Om's T-shirt, caption highlights and anything "safe or accepted" (the glowing home, the confidence glow).
- **Danger colour:** red `#E03131`, used only for rejection elements (the 10 km tape, "नाही", "तू नको", the "लाजरा" label, the liking-gap glow).
- **Font:** Mukta (Google Fonts), 700 weight for captions and 600 for on-screen labels. It renders Devanagari cleanly.

## 2. Character sheet

| Name | Role | Colour | Defining feature | Personality / default expression |
|---|---|---|---|---|
| **ओम (Om)** | Main character, age 6 | Black lines, amber `#F08C00` T-shirt (filled torso shape) | Head about 1.3x the size of other kids' heads, big round eyes, 3-line hair tuft on top | Shy and watchful. Default: **worried** |
| **Adult Om** | Om grown up (scenes 15-17) | Black lines, amber tie | Same hair tuft, taller body | Forced **big grin** outside, small Om hiding inside |
| **आई (Aai)** | Om's mother | Dark blue `#1C3D5A` dress (trapezoid) | Hair bun (circle on the back of the head) | Warm and calm. Default: **happy** |
| **बाबा (Baba)** | Om's father | Green `#2F9E44` shirt | Round glasses (two small circles) | Playful. Default: **big grin** |
| **Park kids (5)** | The group Om wants to join | Black lines | Each wears a cap in one flat colour: red, blue, green, purple, teal | Default: **happy**, running |
| **Two adults** | Liking-gap demo (scenes 38-40) | Black lines | One has a scarf, one has a cap | Default: **happy**, talking |
| **Students / teacher / researcher** | Downey experiment (scenes 51-54) | Black lines | Teacher holds a clipboard, researcher wears a lab coat outline | Default: **neutral** |
| **Counselor** | Scene 90 | Black lines | Small notebook, potted plant beside them | Default: **neutral**, calm |

**Researcher cards:** never draw real researchers. Show a flat card with a clipboard icon, the name and the year as text only.

## 3. Props (simple shapes)

| Prop | How to draw it |
|---|---|
| Park | Green ground line, one lollipop tree (circle on a rectangle) |
| Bench | Two rectangles on two short legs |
| Ball | Circle with one curved seam line |
| 10 km tape | Long red rounded rectangle with white tick marks, label at the centre |
| Footprints | Small grey ovals in pairs |
| Thought bubble | Cloud shape (overlapping circles) with 3 small trailing circles |
| Balance scale | Vertical line, horizontal beam, two hanging pans |
| Gauge / meter | Semicircle arc with red-to-amber gradient and a needle |
| Mirror | Rounded rectangle with a thin frame. Fog = blur filter plus a white overlay at 60% opacity |
| Stopwatch | Circle with a button on top and one hand |
| Gavel | Rounded rectangle head on a stick |
| Label sticker | Red rounded rectangle with white text, slightly rotated |
| Loop / cycle | Large circle with 4 nodes and arrowheads between them |
| Home "secure base" | House shape (square plus triangle) with an amber glow |
| Birthday party | 3 balloons (ovals on strings) and a table line |
| Classroom | Blackboard rectangle and 2 desks |
| Researcher card | White card with a thin border, clipboard icon, two lines of text |

## 4. Expression and pose words

Expressions: neutral, happy, big grin, worried, panicked (wide eyes, sweat drop), embarrassed (red cheeks), confused (question mark), shocked (jaw drop), smug, sad, thinking (hand on chin), relieved (exhale puff)
Poses: standing, walking, running, slumped, arms crossed, pointing, shrug, hiding, celebrating
Motion: bounce in, shake, zoom punch, slow push-in, thought bubble pop, split screen, freeze frame

---

## 5. Scene table

| # | Time | VO line (Marathi) | Characters | Pose + expression | Animation | On-screen text | SFX | Background | Transition |
|---|---|---|---|---|---|---|---|---|---|
| **HOOK** | | | | | | | | | |
| 1 | 0:00-0:05 | पार्कमध्ये पाच मुलं बॉल खेळतायत. | Park kids | running, happy | Ball bounces between kids, slow pan right to left | — | soft kids' laughter, ball bounce | Park | cut in |
| 2 | 0:05-0:10 | ओम सहा वर्षांचा आहे. तो बेंचजवळ उभा आहे. | Om | standing, hands behind back, worried | Camera finishes pan on Om, Om bounces in | "ओम, 6" | soft pop | Park + bench | pan |
| 3 | 0:10-0:15 | त्याला फक्त एक शब्द बोलायचाय. "हाय." | Om | worried, mouth slightly open | Thought bubble pops with "हाय", wobbles | **हाय** | pop | Park + bench | — |
| 4 | 0:15-0:20 | ...दहा पावलांचं अंतर आहे. | Om, kids | standing | 10 footprints appear one by one between Om and kids | **10 पावलं** | 10 quick ticks | Park | — |
| 5 | 0:20-0:25 | ...दहा किलोमीटरचं आहे. | Om, kids | panicked, sweat drop | Footprint line stretches, kids slide far right and shrink, a red tape grows with "10 km", slow push-in on Om | **10 km** (red) | stretch whoosh, low heartbeat | Park | freeze frame, 0.5s hold |
| **RELATE** | | | | | | | | | |
| 6 | 0:25-0:30 | तुम्ही पालक असाल तर हा सीन तुम्ही पाहिलाय. | — | — | Party scene wipes in | — | whoosh | Birthday party | wipe |
| 7 | 0:30-0:35 | बर्थडे पार्टीत तुमचं मूल तुमच्या पायाला चिकटून उभं असतं. | Om, Aai | Om hiding behind Aai's leg, worried | Om peeks out, ducks back | — | party murmur | Party | — |
| 8 | 0:35-0:40 | तुम्ही म्हणता, "जा ना, खेळ त्यांच्याबरोबर." | Aai, Om | Aai pointing, happy | Speech bubble pops | "जा ना, खेळ!" | pop | Party | — |
| 9 | 0:40-0:44 | ते मान हलवतं. जागचं हलत नाही. | Om | hiding, head shake | Shake twice | — | small swish | Party | — |
| 10 | 0:44-0:50 | ...पाहुण्यांना सांगून टाकतो, "हा जरा लाजराच आहे." | Aai, guest, Om | Aai embarrassed smile, Om sad | Red "लाजरा" label flies in and sticks on Om's forehead (kept until scene 78) | **लाजरा** | sticker slap | Party | — |
| 11 | 0:50-0:55 | तुम्ही पालक नसाल तरी हा सीन तुम्हाला माहितीये. | Om | neutral | Party fades, park bench flashes back | — | whoosh | Park | dissolve |
| 12 | 0:55-1:00 | कारण कधीतरी तो बेंचजवळचा मुलगा तुम्ही होतात. | Om | thinking | Arrow points at Om | "तुम्ही?" | ding | Park + bench | cut |
| 13 | 1:00-1:05 | नवीन शाळा. नवीन वर्ग. सगळ्यांचे ग्रुप आधीच तयार. | Om, kids | kids happy in 3 groups, Om alone | Circles draw closed around each group | — | chalk draw | Classroom | cut |
| 14 | 1:05-1:12 | तुम्ही टिफिन उघडून एकटे बसलात... | Om | slumped, sad, opening tiffin | Thought bubble: Om waving, group ignoring him with a red X | — | tiffin click | Classroom | — |
| 15 | 1:12-1:17 | मोठं झाल्यावरही हे पूर्ण संपत नाही. | Om → Adult Om | neutral | Om grows into Adult Om, amber tie appears | — | stretch whoosh | Plain | morph |
| 16 | 1:17-1:21 | ऑफिसची पहिली मीटिंग, नवीन सोसायटी, एखादं नेटवर्किंग इव्हेंट. | Adult Om | standing, worried | 3 quick cuts: meeting table, society gate, name tag | "HELLO" on name tag | 3 pops | Office / gate / event | quick cuts |
| 17 | 1:21-1:25 | फरक इतकाच की आता आपण ते चेहऱ्यावर दिसू देत नाही. | Adult Om, small Om inside | Adult: forced big grin. Small Om: hiding | Chest opens like a window, small Om sits on a bench inside | — | soft heartbeat | Office | slow push-in |
| **OM'S HEAD** | | | | | | | | | |
| 18 | 1:25-1:30 | आता त्या दहा सेकंदात ओमच्या डोक्यात काय चाललंय ते बघू. | Om | worried | Zoom into Om's head, which becomes a dotted-outline room | — | zoom whoosh | Inside head | zoom |
| 19 | 1:30-1:35 | "हे मला खेळायला घेतील का?" | Om | thinking | Thought bubble 1 pops | bubble text | pop | Inside head | — |
| 20 | 1:35-1:40 | "मी काही चुकीचं बोललो तर हसतील का?" | Om | embarrassed | Bubble 2 pops, tiny laughing faces around it | bubble text | pop, faint laugh | Inside head | — |
| 21 | 1:40-1:45 | "मी यांचा फ्रेंड होऊ शकतो का?" | Om | worried | Bubble 3 pops | bubble text | pop | Inside head | — |
| 22 | 1:45-1:53 | ...एक प्रश्न असतो...: "मी पुरेसा चांगला आहे का?" | Om | sad | 3 bubbles slide up, one large grey foggy bubble rises from below | **मी पुरेसा चांगला आहे का?** | low drone | Inside head | slow push-in |
| 23 | 1:53-1:58 | मोठ्यांसाठी "हाय" म्हणणं दोन सेकंदांचं काम आहे. | Adult stickman | happy, casual wave | Stopwatch shows 0:02 | "2 सेकंद" | ding | Plain | cut |
| 24 | 1:58-2:02 | मुलासाठी ती एक रिस्क आहे. | Om | panicked | Stopwatch turns into a red warning triangle | **रिस्क** | alert blip | Plain | — |
| 25 | 2:02-2:09 | तो स्वतःला कुणासमोर तरी ठेवतोय... हे त्याच्या हातात नाही. | Om, kids | Om in a spotlight, worried. Kids hold cards behind their backs | Cards flip slowly but stop before showing a side | "हो / नाही ?" | short drumroll | Spotlight stage | — |
| 26 | 2:09-2:14 | लहान मूल "नाही" ऐकतं तेव्हा ते "आत्ता हा खेळ भरलाय" असं ऐकत नाही. | Kid, Om | kid neutral | Speech bubble "नाही" leaves the kid | "नाही" | — | Park | — |
| 27 | 2:14-2:19 | ते "तू नको" असं ऐकतं. | Om | shocked, then sad | Bubble travels to Om's ear and morphs from "नाही" into red "तू नको" | **तू नको** | glitch whoosh | Park | — |
| 28 | 2:19-2:26 | म्हणून त्याच्या मनाला वाटतं की न विचारलेलंच बरं... | Om | thinking | Balance scale: small "हाय" vs a big red rock "नकार". Scale tips to "नकार" | "हाय" vs **नकार** | heavy thud | Plain | cut |
| 29 | 2:26-2:35 | ओम दोन पावलं पुढे जातो. थांबतो. परत बेंचजवळ येतो. | Om | walking, freeze, walking back slumped | Footprints: 2 forward, pause, 2 back | — | 2 steps, silence, 2 steps | Park + bench | cut |
| **TEMPERAMENT** | | | | | | | | | |
| 30 | 2:35-2:42 | पहिली गोष्ट क्लिअर करूया... प्रॉब्लेम आहे, असं नाही. | Om | sad, then relieved | Red "प्रॉब्लेम?" stamp, struck through | ~~प्रॉब्लेम~~ | eraser swipe | Plain | cut |
| 31 | 2:42-2:49 | हार्वर्डचे सायकॉलॉजिस्ट जेरोम केगन... | Researcher card | — | Card slides in | "जेरोम केगन, हार्वर्ड / Kagan et al., 1988" | paper slide | Plain | slide |
| 32 | 2:49-2:57 | काही मुलं अगदी लहानपणापासून... जास्त सावध असतात. | 2 babies | Baby 1 happy. Baby 2 thinking, looks back at mother first | Baby 1 crawls fast to a toy block. Baby 2 pauses, then crawls slowly | — | soft pop | Nursery rug | — |
| 33 | 2:57-3:04 | "बिहेवियरल इनहिबिशन"... आधी बघायचं, मग जायचं. | Baby 2 | thinking | Text writes on | **आधी बघायचं, मग जायचं** | ding | Nursery | — |
| 34 | 3:04-3:08 | हा स्वभाव आहे, दोष नाही. | Baby 2 | happy | "दोष" fades, amber "स्वभाव" stamps in | **स्वभाव** | stamp | Nursery | — |
| 35 | 3:08-3:17 | ...दगडावरची रेघ नसतो... बरीच मुलं हळूहळू मोकळी होतात. | Baby 2 growing up | relieved, then happy | Grows through 3 sizes and gradually joins a group | — | gentle rising tone | Park | — |
| 36 | 3:17-3:25 | स्वभावाबरोबर अजून एक गोष्ट काम करते... | Om | thinking | Om looks into a small hand mirror (sets up the mirror metaphor) | "मी कसा आहे?" | soft chime | Plain | slow push-in |
| **LIKING GAP** | | | | | | | | | |
| 37 | 3:25-3:31 | 2018 मध्ये एरिका बूथबी आणि त्यांच्या टीमने... | Researcher card | — | Card slides in | "Boothby et al., 2018" | paper slide | Plain | slide |
| 38 | 3:31-3:39 | दोन अनोळखी माणसं गप्पा मारतात... | Two adults | happy, talking | Speech bubbles alternate | — | soft chatter | Café table, 2 cups | — |
| 39 | 3:39-3:47 | बहुतेक लोकांनी हा आकडा कमी सांगितला. प्रत्यक्षात... जास्त आवडले होते. | Two adults | A worried, B happy | Gauges above heads: "मला तो किती आवडला" 8/10, "मी त्याला किती आवडलो" 5/10 | gauge labels | meter tick | Café | — |
| 40 | 3:47-3:52 | याला "लायकिंग गॅप" म्हणतात. | — | — | The gap between the needles glows red | **लायकिंग गॅप** | zoom punch hit | Café | zoom punch |
| 41 | 3:52-4:00 | 2021 मध्ये वूटर वुल्फ, नाफे आणि मायकल टोमासेलो... | Researcher card | — | Card slides in | "Wolf, Nafe & Tomasello, 2021 / वय 4-11" | paper slide | Plain | slide |
| 42 | 4:00-4:07 | चार वर्षांच्या मुलांमध्ये हा गॅप दिसला नाही... | 4-year-old | big grin | Both gauges at 9, no gap | "वय 4: गॅप नाही" | happy ding | Plain | — |
| 43 | 4:07-4:16 | हा गॅप साधारण पाच वर्षांच्या वयात सुरू होतो... | 5-year-old | worried, looks over shoulder at whispering kids | Age timeline appears, marker at 5, gap opens slightly | **वय 5** | tick | Timeline | — |
| 44 | 4:16-4:22 | आणि वय वाढतं तसा हा गॅप मोठा होत जातो. | 11-year-old | sad | Marker slides to 11, gap widens | "वय 11" | stretch whoosh | Timeline | — |
| 45 | 4:22-4:31 | म्हणजे ओमला जे वाटतंय की "ते मला घेणार नाहीत", ते बऱ्याचदा सत्य नसतं. | Om, kids | Om worried. Kids are waving at him | Thought bubble "ते मला घेणार नाहीत" blocks Om's view, then turns transparent to reveal kids waving | bubble text | pop | Park | — |
| 46 | 4:31-4:40 | तो त्याच्या मनातला अंदाज असतो... स्वतःच्या विरोधात असतो. | Om | confused | Arrow from Om's head curves back and points at Om | "अंदाज ≠ सत्य" | — | Park | cut |
| **REJECTION LOOP** | | | | | | | | | |
| 47 | 4:40-4:45 | हा अंदाज कधी कधी स्वतःच खरा ठरतो. | Om | worried | Thought bubble hardens into stone | — | stone thud | Plain | — |
| 48 | 4:45-4:52 | कोलंबिया युनिव्हर्सिटीच्या... जेराल्डिन डाउनी... | Researcher card | — | Card slides in | "जेराल्डिन डाउनी, कोलंबिया / रिजेक्शन सेन्सिटिव्हिटी" | paper slide | Plain | slide |
| 49 | 4:52-4:58 | म्हणजे नकार मिळेल याची सतत भीती... | Om | panicked | Radar on Om's head pings at small things: a kid yawns, a kid turns away | — | radar ping x3 | Park | — |
| 50 | 4:58-5:04 | 1998 मध्ये त्यांनी पाचवी ते सातवीतल्या मुलांवर... | Researcher card | — | Card slides in | "Downey et al., 1998 / इयत्ता 5-7" | paper slide | Classroom | slide |
| 51 | 5:04-5:10 | मुलांना सांगितलं... मित्राला इंटरव्ह्यूसाठी बोलवा. | Student | happy, holding invite card | Walks to a door | — | footsteps | School corridor | — |
| 52 | 5:10-5:16 | ...तो मित्र यायला तयार नाही. का, ते सांगितलं नाही. | Researcher, student | Researcher shrug. Student shocked | "?" floats up | "?" | soft record scratch | Corridor | — |
| 53 | 5:16-5:24 | ज्या मुलांना आधीपासूनच नकाराची भीती जास्त होती... जास्त अस्वस्थ झाली. | 2 students | Left: slightly sad. Right: panicked with shake | Split screen. Right student's "अस्वस्थता" gauge is higher | "अस्वस्थता" | heartbeat | Corridor | split screen |
| 54 | 5:24-5:31 | ...शिक्षकांच्या रिपोर्टनुसार... वर्षभरानंतर... जास्त अडचणी आल्या. | Teacher | thinking, holding report | Calendar flips 12 pages, report shows a falling line | "1 वर्षानंतर" | page flips | Classroom | — |
| 55 | 5:31-5:35 | हे एक चक्र आहे. | — | — | Large circle draws on with 4 empty nodes | **चक्र** | draw sound | Plain | — |
| 56 | 5:35-5:41 | "ते मला नाकारतील" असं वाटलं की मूल लांब राहतं... | Om | arms crossed, standing apart, worried | Nodes 1 and 2 fill in | "ते मला नाकारतील" → "मी लांब राहतो" | pop, pop | Loop | — |
| 57 | 5:41-5:47 | समोरच्या मुलांना ते दूरचं वाटतं... बोलवत नाहीत. | Kids | neutral, turning away | Node 3 fills in | "ते बोलवत नाहीत" | pop | Loop | — |
| 58 | 5:47-5:53 | ...मनात पक्कं होतं, "बघ, मी म्हटलं होतं ना." | Om | sad | Node 4 fills in. The loop spins and Om shrinks a little on each lap | "बघ, मी म्हटलं होतं" | spin whoosh | Loop | — |
| 59 | 5:53-6:00 | नकार बाहेरून येण्याआधी... स्वतःला मनात आधीच नाकारलेलं असतं. | Om | sad, holding a red "नाही" board facing himself | Hold | **नाही** | single soft thud | Plain | freeze frame |
| **SELF-ACCEPTANCE** | | | | | | | | | |
| 60 | 6:00-6:08 | इथे दोन गोष्टी एकमेकांना जोडलेल्या आहेत... | Om | thinking | Two circles, "मी स्वतःला कसं पाहतो" and "इतर मला कसं स्वीकारतात", joined by a chain link | both labels | chain clink | Plain | — |
| 61 | 6:08-6:14 | 1995 मध्ये मार्क लिअरी... "सोशिओमीटर थिअरी" मांडली. | Researcher card | — | Card slides in | "Leary et al., 1995 / सोशिओमीटर" | paper slide | Plain | slide |
| 62 | 6:14-6:22 | ...आत्मसन्मान एका मीटरसारखा काम करतो... | Om | neutral | Gauge appears on Om's chest, needle wobbling | "स्वीकारला जातोय का?" | meter tick | Plain | — |
| 63 | 6:22-6:26 | हा मीटर दोन्ही बाजूंनी चालतो. | Om | neutral | Two-way arrow circles the gauge | — | whoosh | Plain | — |
| 64 | 6:26-6:31 | लोकांनी स्वीकारलं की मीटर वर जातो. | Om, kid | Kid high-fives Om, Om happy | Needle rises into amber | — | rising tone | Park | — |
| 65 | 6:31-6:39 | ...मीटर आधीच खाली असेल, तर... प्रत्येक दुर्लक्षात नकार वाचतं. | Om, kids | Om worried. Kids neutral, one silent, one looking away | Needle low. Small red "नकार?" tags pop over each neutral action | "नकार?" x3 | pop x3 | Park | — |
| 66 | 6:39-6:48 | ज्या मुलाने मनापासून मानलंय की "मी जसा आहे तसा ठीक आहे"... | Om (amber outline glow) | happy, shrug | Group 1 says "नाही". Om shrugs and walks to group 2, who welcome him | **मी ठीक आहे** | light pop | Park, 2 groups | — |
| 67 | 6:48-6:56 | ज्याने स्वतःला स्वीकारलेलं नाही... त्याच्याबद्दलचा निकाल असतो. | Om | shocked | "नाही" turns into a gavel that slams down "निकाल" | **निकाल** | gavel bang | Plain | zoom punch |
| 68 | 6:56-7:00 | याला एका आरशासारखं बघा. | — | — | Mirror draws on | **आरसा** | shimmer | Plain | — |
| 69 | 7:00-7:07 | मूल इतरांकडे बघतं तेव्हा त्याला स्वतःबद्दलचं मतच परत दिसतं. | Om | worried | Om looks at the kids, a mirror sits between them and shows Om's own face | — | shimmer | Park | — |
| 70 | 7:07-7:14 | आरसा धूसर असेल, तर... साधं हसणंसुद्धा थट्टेसारखं वाटतं. | Om, kids (in mirror) | Real kids happy. In the fogged mirror they look smug | Fog blur over the mirror | — | distorted laugh | Park | — |
| 71 | 7:14-7:20 | हा आरसा सुरुवातीला मूल स्वतः साफ करू शकत नाही. ते काम घरचे लोक करतात. | Aai, Baba, Om | Aai and Baba happy, wiping the mirror with a cloth | Wipe clears the fog, kids now just smile | — | squeaky wipe | Home: window, sofa | — |
| 72 | 7:20-7:26 | कार्ल रॉजर्स याला "अनकंडिशनल पॉझिटिव्ह रिगार्ड" म्हणायचे. | Researcher card | — | Card slides in | "Carl Rogers / अनकंडिशनल पॉझिटिव्ह रिगार्ड" | paper slide | Plain | slide |
| 73 | 7:26-7:35 | ...प्रेम मार्क्स, परफॉर्मन्स किंवा तो किती बोलका आहे यावर अवलंबून नाही. | Aai, Om | Aai hugging Om, both happy | Tags "मार्क्स", "परफॉर्मन्स", "बोलका?" float off and fade. An amber heart stays | 3 tags | pop x3, soft chime | Home | — |
| 74 | 7:35-7:45 | असं प्रेम मिळालेलं मूल... "सिक्युअर बेस" म्हणतात. | Om, home | Om walking out happy, looks back once | House glows amber, dotted path from house to park | **सिक्युअर बेस** | warm chime | Home → park | pan |
| **WHAT PARENTS CAN DO** | | | | | | | | | |
| 75 | 7:45-7:50 | पालक म्हणून तीन गोष्टी आजपासून करता येतील. | — | — | 3 cards stack with numbers 1, 2, 3 | "पालकांसाठी 3 गोष्टी" | card shuffle | Plain | — |
| 76 | 7:50-7:55 | एक. मुलाला लेबल लावू नका. | Om (red "लाजरा" label from scene 10) | sad | Card 1 flips | "1. लेबल नको" | flip | Plain | — |
| 77 | 7:55-8:02 | "हा लाजरा आहे" हे वाक्य मूल वारंवार ऐकतं... ओळख बनू शकतं. | Om | sad | Label grows, Om shrinks under it | **लाजरा** | — | Plain | — |
| 78 | 8:02-8:10 | त्याऐवजी म्हणा, "त्याला आधी थोडा वेळ बघायला आवडतं."... | Aai, Om | Aai peels the label off. Om relieved | Label peels away, replaced by a small amber bubble | "आधी बघायला आवडतं" | peel sound | Party (callback) | — |
| 79 | 8:10-8:14 | दोन. "हाय" छोट्या स्टेप्समध्ये शिकवा. | — | — | Card 2 flips | "2. छोट्या स्टेप्स" | flip | Plain | — |
| 80 | 8:14-8:20 | घरी रोल प्ले करा... | Baba, Om | Baba big grin, Om shy | Baba puts on a cap and a sign "नवीन मुलगा" | "नवीन मुलगा" | pop | Home sofa | — |
| 81 | 8:20-8:27 | "माझं नाव ओम. मला बॉल खेळायला आवडतं. मी पण खेळू का?" | Om | happy, hand forward | Speech bubble, 3 lines appear one by one | 3 lines | pop x3 | Home | — |
| 82 | 8:27-8:33 | तीन वाक्यं. घरी दहा वेळा म्हटली की बाहेर एकदा म्हणणं सोपं जातं. | Om | celebrating (small) | Tally marks count 1 to 10, then an arrow points to the park | "10 वेळा घरी = 1 वेळा बाहेर" | tally ticks | Home | — |
| 83 | 8:33-8:40 | ...आधी एका मुलाशी ओळख, मग ग्रुप. | Om, 1 kid, group | happy | Om talks to one kid, then both join the group | "आधी 1, मग ग्रुप" | pop | Park | — |
| 84 | 8:40-8:44 | तीन. प्रयत्नाचं कौतुक करा, निकालाचं नाही. | — | — | Card 3 flips | "3. प्रयत्न > निकाल" | flip | Plain | — |
| 85 | 8:44-8:52 | ...तरी म्हणा, "तू स्वतः जाऊन बोललास, हे मला खूप आवडलं." | Om, Aai | Om walks back sad, Aai happy, high-five | Spark on the high-five | "तू स्वतः जाऊन बोललास" | high-five clap | Park | — |
| 86 | 8:52-8:58 | ...त्याची किंमत समोरच्याच्या "हो" वर ठरत नाही. | Om | relieved | A "नाही" bubble bounces off Om. His chest gauge stays steady | — | boing | Plain | — |
| 87 | 8:58-9:04 | आणि मुलं आपल्याला बघून शिकतात. | Aai, Baba, neighbour, Om | Aai and Baba happy, greeting a new neighbour. Om watches from behind | — | — | doorbell | Apartment door | — |
| 88 | 9:04-9:10 | तुम्ही नवीन लोकांशी कसं बोलता, स्वतःच्या चुकांबद्दल कसं बोलता... | Baba, Om | Baba embarrassed, then laughing at spilled tea | Tea spill | "चुकलो, चालतंय" | splash | Kitchen | — |
| 89 | 9:10-9:16 | तुम्ही स्वतःला स्वीकारलं, तर त्याला ते शिकवणं खूप सोपं जातं. | Baba, Om | Om copies Baba's laugh, both happy | Mirror-pose | — | soft chime | Kitchen | — |
| 90 | 9:16-9:25 | भीती खूप जास्त असेल... चाइल्ड सायकॉलॉजिस्टशी नक्की बोला. | Aai, Om, counselor | calm, neutral | Gentle fade in, info card | "भीती खूप जास्त असेल तर चाइल्ड सायकॉलॉजिस्टचा सल्ला घ्या" | none (music dips) | Counselor office, plant | fade |
| **CLOSE** | | | | | | | | | |
| 91 | 9:25-9:31 | तोच पार्क. तोच बेंच. तीच दहा पावलं. | Om, kids | standing, worried | Repeats scene 5's framing with the red "10 km" tape | "10 km" | soft heartbeat | Park + bench | match cut |
| 92 | 9:31-9:36 | ओम पुढे जातो. आवाज थोडा थरथरतो. | Om | walking, slight shake | Footprints appear as he walks. Tape shrinks from "10 km" to amber "10 पावलं" | **10 पावलं** | footsteps | Park | — |
| 93 | 9:36-9:41 | "हाय. मी ओम. मी पण खेळू का?" | Om | worried, then hopeful, hand up | Speech bubble | **हाय** | — | Park | slow push-in |
| 94 | 9:41-9:45 | एक मुलगा बॉल त्याच्याकडे फेकतो. | Kid, Om | Kid big grin throws. Om catches, big grin | Ball arc | — | ball whoosh, catch thump, kids cheer | Park | — |
| 95 | 9:45-9:50 | ते दहा किलोमीटरचं अंतर दहा पावलांचंच होतं. | All kids, Om | celebrating | Camera rises, 6 kids playing together | — | music swell | Park wide | crane up |
| 96 | 9:50-9:55 | ...हा व्हिडिओ त्याच्या आई-बाबांना पाठवा. | — | — | Share arrow icon | "आई-बाबांना पाठवा" | pop | Plain | — |
| 97 | 9:55-10:00 | ...लायकिंग गॅपवर वेगळा व्हिडिओ हवा असेल, तर कमेंटमध्ये सांगा. | Om | happy, waving | Comment bubble icon, then hold for end screen | "कमेंटमध्ये सांगा" | pop, music out | Plain | end screen (leave right 40% empty for 20s end-screen elements if extended) |

---

## 6. Captions

- Word-by-word animated captions across the whole video, timed from the voiceover audio.
- Lower third, centred, Mukta 700, 60px, black `#1A1A1A` with a 4px off-white stroke. Max 2 lines.
- Key words turn amber `#F08C00` with a small scale pop. Rejection words turn red `#E03131`.
- **Amber words:** हाय, 10 पावलं, स्वभाव, लायकिंग गॅप, सोशिओमीटर, आरसा, सिक्युअर बेस, प्रयत्न, मी ठीक आहे
- **Red words:** 10 km, लाजरा, रिस्क, तू नको, नकार, निकाल, चक्र, रिजेक्शन सेन्सिटिव्हिटी
- Hide captions while a researcher card is on screen if they overlap. Move them to the top third instead.

## 7. Audio plan

**Voiceover**
- Marathi, warm, calm, mid-low male voice, like a parent telling a story. About 105-110 words per minute.
- Best option: Shrikant records it himself. It suits a personal-brand channel and avoids TTS mispronouncing Marathi words.
- TTS fallback: check that the voice model actually supports Marathi before generating. HyperFrames' local TTS may not. ElevenLabs is connected and is an option if its model lists Marathi. Listen to one test paragraph first, especially for "ळ", "ऱ्या" and the English loanwords.
- Pauses (marked `(pause)` in the handoff script): after "दहा किलोमीटरचं आहे", after "मी पुरेसा चांगला आहे का?", after "परत बेंचजवळ येतो", after "आधीच नाकारलेलं असतं", before "तोच पार्क", and after "दहा पावलांचंच होतं". Each one lasts 0.8-1.2s.
- Caption timing: transcribe the final VO with Whisper (it supports Marathi), or force-align it to the known script for cleaner word timings.

**Music**
- Gentle piano with soft acoustic guitar, warm and slightly wistful, no lyrics. Royalty-free (YouTube Audio Library or Pixabay Music).
- Sits at about -22 dB under the voice, ducked further while the voice is speaking.
- Changes: thins out from 4:40-6:00 (the rejection loop), warms up from 6:00 (self-acceptance), dips to near silence in scene 90, swells at scene 95, fades out at 10:00.

**SFX** (short and quiet, always below the voice)
ball bounce (1, 94), kids' laughter (1, 20), pop (2, 3, 8, 19-21, 45, 56-57, 65-66, 73, 80-81, 83, 96-97), tick (4, 39, 43, 62), stretch whoosh (5, 15, 44), heartbeat (5, 17, 53, 91), whoosh (6, 11, 18, 63), party murmur (7), swish (9), sticker slap (10), ding (12, 23, 33, 42), chalk draw (13), tiffin click (14), drone (22), alert blip (24), drumroll (25), glitch whoosh (27), thud (28, 47, 59), footsteps (29, 51, 92), eraser (30), paper slide (31, 37, 41, 48, 50, 61, 72), stamp (34), rising tone (35, 64), chime (36, 73, 74, 89), chatter (38), zoom punch hit (40, 67), radar ping (49), record scratch (52), page flips (54), draw (55), spin whoosh (58), chain clink (60), distorted laugh (70), squeaky wipe (71), card shuffle and flip (75, 76, 79, 84), peel (78), tally ticks (82), clap (85), boing (86), doorbell (87), splash (88), gavel (67), catch thump and cheer (94).


## 8. Script (voiceover, Marathi)

[[0:00-0:25] HOOK]
पार्कमध्ये पाच मुलं बॉल खेळतायत.
ओम सहा वर्षांचा आहे. तो बेंचजवळ उभा आहे.
त्याला फक्त एक शब्द बोलायचाय. "हाय."
त्याच्यात आणि त्या मुलांमध्ये दहा पावलांचं अंतर आहे.
पण ओमच्या मनात हे अंतर दहा किलोमीटरचं आहे. (pause)

[[0:25-1:25] RELATE]
तुम्ही पालक असाल तर हा सीन तुम्ही पाहिलाय.
बर्थडे पार्टीत तुमचं मूल तुमच्या पायाला चिकटून उभं असतं.
तुम्ही म्हणता, "जा ना, खेळ त्यांच्याबरोबर."
ते मान हलवतं. जागचं हलत नाही.
आणि आपण नकळत पाहुण्यांना सांगून टाकतो, "हा जरा लाजराच आहे."

तुम्ही पालक नसाल तरी हा सीन तुम्हाला माहितीये.
कारण कधीतरी तो बेंचजवळचा मुलगा तुम्ही होतात.
नवीन शाळा. नवीन वर्ग. सगळ्यांचे ग्रुप आधीच तयार.
तुम्ही टिफिन उघडून एकटे बसलात, कारण जाऊन बोललो आणि त्यांनी दुर्लक्ष केलं तर काय, ही भीती होती.

मोठं झाल्यावरही हे पूर्ण संपत नाही.
ऑफिसची पहिली मीटिंग, नवीन सोसायटी, एखादं नेटवर्किंग इव्हेंट.
फरक इतकाच की आता आपण ते चेहऱ्यावर दिसू देत नाही.

[[1:25-2:35] ओमच्या डोक्यात काय चाललंय]
आता त्या दहा सेकंदात ओमच्या डोक्यात काय चाललंय ते बघू.
"हे मला खेळायला घेतील का?"
"मी काही चुकीचं बोललो तर हसतील का?"
"मी यांचा फ्रेंड होऊ शकतो का?"
आणि या सगळ्याच्या खाली एक प्रश्न असतो, जो त्याला शब्दांत सांगता येत नाही: "मी पुरेसा चांगला आहे का?" (pause)

मोठ्यांसाठी "हाय" म्हणणं दोन सेकंदांचं काम आहे.
मुलासाठी ती एक रिस्क आहे.
तो स्वतःला कुणासमोर तरी ठेवतोय, आणि समोरचा "हो" म्हणेल की "नाही", हे त्याच्या हातात नाही.

लहान मूल "नाही" ऐकतं तेव्हा ते "आत्ता हा खेळ भरलाय" असं ऐकत नाही.
ते "तू नको" असं ऐकतं.
म्हणून त्याच्या मनाला वाटतं की न विचारलेलंच बरं. विचारलंच नाही तर नकारही मिळणार नाही.

ओम दोन पावलं पुढे जातो. थांबतो. परत बेंचजवळ येतो. (pause)

[[2:35-3:25] हा दोष नाही, स्वभाव आहे]
पहिली गोष्ट क्लिअर करूया. असं होतंय म्हणजे मुलात काही प्रॉब्लेम आहे, असं नाही.
हार्वर्डचे सायकॉलॉजिस्ट जेरोम केगन यांनी अनेक वर्षं लहान मुलांचा अभ्यास केला.
त्यांना दिसलं की काही मुलं अगदी लहानपणापासून नवीन माणसं आणि नवीन जागांबद्दल जास्त सावध असतात.
त्यांनी याला "बिहेवियरल इनहिबिशन" म्हटलं. सोप्या भाषेत, आधी बघायचं, मग जायचं.
हा स्वभाव आहे, दोष नाही.
आणि केगन यांच्या अभ्यासात हेही दिसलं की हा स्वभाव दगडावरची रेघ नसतो. वातावरण आणि घरचा आधार मिळाला तर बरीच मुलं हळूहळू मोकळी होतात.

स्वभावाबरोबर अजून एक गोष्ट काम करते: मूल स्वतःबद्दल काय विचार करतं.

[[3:25-4:40] PROOF 1: लायकिंग गॅप]
2018 मध्ये एरिका बूथबी आणि त्यांच्या टीमने मोठ्या माणसांवर एक अभ्यास केला.
दोन अनोळखी माणसं गप्पा मारतात. नंतर प्रत्येकाला विचारलं जातं, "समोरच्याला तुम्ही किती आवडलात?"
बहुतेक लोकांनी हा आकडा कमी सांगितला. प्रत्यक्षात समोरच्याला ते जास्त आवडले होते.
याला "लायकिंग गॅप" म्हणतात.

2021 मध्ये वूटर वुल्फ, नाफे आणि मायकल टोमासेलो यांनी हाच प्रयोग चार ते अकरा वर्षांच्या मुलांवर केला.
चार वर्षांच्या मुलांमध्ये हा गॅप दिसला नाही. त्यांना वाटतं, मला सगळेच आवडतात आणि मीही सगळ्यांना आवडतो.
हा गॅप साधारण पाच वर्षांच्या वयात सुरू होतो. याच वयात मुलं "लोक माझ्याबद्दल काय विचार करतात" याचा विचार करायला लागतात.
आणि वय वाढतं तसा हा गॅप मोठा होत जातो.

म्हणजे ओमला जे वाटतंय की "ते मला घेणार नाहीत", ते बऱ्याचदा सत्य नसतं.
तो त्याच्या मनातला अंदाज असतो, आणि तो अंदाज बहुतेक वेळा स्वतःच्या विरोधात असतो.

[[4:40-6:00] PROOF 2: नकाराची भीती स्वतःच खरी कशी ठरते]
हा अंदाज कधी कधी स्वतःच खरा ठरतो.
कोलंबिया युनिव्हर्सिटीच्या सायकॉलॉजिस्ट जेराल्डिन डाउनी यांनी याला "रिजेक्शन सेन्सिटिव्हिटी" म्हटलं.
म्हणजे नकार मिळेल याची सतत भीती, आणि छोट्याशा संकेतातही नकार दिसणं.

1998 मध्ये त्यांनी पाचवी ते सातवीतल्या मुलांवर एक प्रयोग केला.
मुलांना सांगितलं की तुमच्या वर्गातल्या एका मित्राला इंटरव्ह्यूसाठी बोलवा.
थोड्या वेळाने त्यांना सांगितलं गेलं की तो मित्र यायला तयार नाही. का, ते सांगितलं नाही.
ज्या मुलांना आधीपासूनच नकाराची भीती जास्त होती, ती या साध्याशा, अस्पष्ट नकाराने जास्त अस्वस्थ झाली.
आणि शिक्षकांच्या रिपोर्टनुसार, अशा मुलांना वर्षभरानंतर मित्रांच्या बाबतीत जास्त अडचणी आल्या.

हे एक चक्र आहे.
"ते मला नाकारतील" असं वाटलं की मूल लांब राहतं, किंवा खूप ताणून, अवघडून वागतं.
समोरच्या मुलांना ते दूरचं वाटतं, म्हणून ते त्याला बोलवत नाहीत.
आणि मुलाच्या मनात पक्कं होतं, "बघ, मी म्हटलं होतं ना."
नकार बाहेरून येण्याआधी, त्याने स्वतःला मनात आधीच नाकारलेलं असतं. (pause)

[[6:00-7:45] स्वतःला स्वीकारणं आणि इतरांनी स्वीकारणं]
इथे दोन गोष्टी एकमेकांना जोडलेल्या आहेत: मूल स्वतःला कसं पाहतं, आणि इतर त्याला कसं स्वीकारतात.
1995 मध्ये मार्क लिअरी या सायकॉलॉजिस्टने "सोशिओमीटर थिअरी" मांडली.
त्यांच्या मते आपला आत्मसन्मान एका मीटरसारखा काम करतो. तो सतत मोजत असतो, "मी लोकांमध्ये स्वीकारला जातोय का?"

हा मीटर दोन्ही बाजूंनी चालतो.
लोकांनी स्वीकारलं की मीटर वर जातो.
आणि मीटर आधीच खाली असेल, तर मूल प्रत्येक शांततेत, प्रत्येक दुर्लक्षात नकार वाचतं.

ज्या मुलाने मनापासून मानलंय की "मी जसा आहे तसा ठीक आहे", त्याच्यासाठी "नाही" म्हणजे फक्त एका खेळाचा "नाही". तो दुसऱ्या ग्रुपकडे जातो.
ज्याने स्वतःला स्वीकारलेलं नाही, त्याच्यासाठी प्रत्येक "नाही" हा त्याच्याबद्दलचा निकाल असतो.

याला एका आरशासारखं बघा.
मूल इतरांकडे बघतं तेव्हा त्याला स्वतःबद्दलचं मतच परत दिसतं.
आरसा धूसर असेल, तर समोरच्याचं साधं हसणंसुद्धा थट्टेसारखं वाटतं.

हा आरसा सुरुवातीला मूल स्वतः साफ करू शकत नाही. ते काम घरचे लोक करतात.
कार्ल रॉजर्स याला "अनकंडिशनल पॉझिटिव्ह रिगार्ड" म्हणायचे. म्हणजे मुलाला हे जाणवणं की त्याच्यावरचं प्रेम मार्क्स, परफॉर्मन्स किंवा तो किती बोलका आहे यावर अवलंबून नाही.
असं प्रेम मिळालेलं मूल बाहेरचं जग एक्सप्लोर करायला जास्त तयार असतं, कारण परत यायला एक सुरक्षित जागा आहे हे त्याला माहीत असतं. अटॅचमेंट रिसर्चमध्ये याला "सिक्युअर बेस" म्हणतात.

[[7:45-9:25] पालक म्हणून काय करता येईल]
पालक म्हणून तीन गोष्टी आजपासून करता येतील.

एक. मुलाला लेबल लावू नका.
"हा लाजरा आहे" हे वाक्य मूल वारंवार ऐकतं, तेव्हा ते त्याची ओळख बनू शकतं.
त्याऐवजी म्हणा, "त्याला आधी थोडा वेळ बघायला आवडतं." हे खरंही आहे, आणि त्यात दोषही नाही.

दोन. "हाय" छोट्या स्टेप्समध्ये शिकवा.
घरी रोल प्ले करा. तुम्ही नवीन मुलगा बना, आणि मूल स्वतःची ओळख करून देईल.
"माझं नाव ओम. मला बॉल खेळायला आवडतं. मी पण खेळू का?"
तीन वाक्यं. घरी दहा वेळा म्हटली की बाहेर एकदा म्हणणं सोपं जातं.
आणि लगेच मोठ्या ग्रुपमध्ये ढकलू नका. आधी एका मुलाशी ओळख, मग ग्रुप.

तीन. प्रयत्नाचं कौतुक करा, निकालाचं नाही.
मूल जाऊन हाय म्हणालं आणि समोरच्यांनी खेळायला घेतलं नाही, तरी म्हणा, "तू स्वतः जाऊन बोललास, हे मला खूप आवडलं."
यातून मुलाला कळतं की त्याची किंमत समोरच्याच्या "हो" वर ठरत नाही.

आणि मुलं आपल्याला बघून शिकतात.
तुम्ही नवीन लोकांशी कसं बोलता, स्वतःच्या चुकांबद्दल कसं बोलता, ते मूल रोज बघतं.
तुम्ही स्वतःला स्वीकारलं, तर त्याला ते शिकवणं खूप सोपं जातं.

भीती खूप जास्त असेल, मूल शाळेत जायला सतत घाबरत असेल किंवा रोजच्या आयुष्यावर परिणाम होत असेल, तर चाइल्ड सायकॉलॉजिस्टशी नक्की बोला.

[[9:25-10:00] CLOSE]
(pause) तोच पार्क. तोच बेंच. तीच दहा पावलं.
ओम पुढे जातो. आवाज थोडा थरथरतो.
"हाय. मी ओम. मी पण खेळू का?"
एक मुलगा बॉल त्याच्याकडे फेकतो.
ते दहा किलोमीटरचं अंतर दहा पावलांचंच होतं. (pause)

तुमच्या ओळखीत एखादा ओम असेल, तर हा व्हिडिओ त्याच्या आई-बाबांना पाठवा.
आणि मोठ्या माणसांमधल्या लायकिंग गॅपवर वेगळा व्हिडिओ हवा असेल, तर कमेंटमध्ये सांगा.

## 9. Steps

1. Init the project.
2. Build reusable SVG components first: Om, Adult Om, Aai, Baba, generic kid (cap colour prop), researcher card, gauge, mirror, thought bubble, 10 km tape, loop diagram.
3. Build the composition scene by scene from the table.
4. Lint.
5. Preview, and show me the preview (especially scenes 1-5, 27, 58-59 and 91-95) before the final render.
6. Render to MP4 at output/child-saying-hi.mp4.
