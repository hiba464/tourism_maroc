console.log("Tourism Maroc Loaded");
let allHotels = [];
/* Cursor Glow */
const glow = document.querySelector(".cursor-glow");

if (glow) {

    document.addEventListener("mousemove", (e) => {

        glow.style.left =
            (e.clientX - 150) + "px";

        glow.style.top =
            (e.clientY - 150) + "px";

    });

}


/* Load Hotels */

async function loadHotels() {

    try {

        const response =
            await fetch(
                "http://127.0.0.1:5000/hotels"
            );

        const hotels =
            await response.json();

            allHotels = hotels;

        const container =
            document.getElementById(
                "hotels-container"
            );

        const hotelSelect =
            document.getElementById(
                "hotel"
            );


            const reviewHotel =
            document.getElementById(
              "reviewHotel"
            );

             container.innerHTML = "";
             hotelSelect.innerHTML = "";

             if(reviewHotel){
             reviewHotel.innerHTML = "";
}

         
        hotels.forEach(hotel => {

            hotelSelect.innerHTML += `

            <option value="${hotel.name}">
                ${hotel.name}
            </option>

            `;

        if(reviewHotel){

    reviewHotel.innerHTML += `

    <option value="${hotel.name}">
        ${hotel.name}
    </option>

    `;

}

            container.innerHTML += `

            <div class="card hotel-card">

                <div
                class="favorite"
                onclick="toggleFavorite(this)">
                    ❤
                </div>

                <img
                src="${hotel.image}"
                alt="${hotel.name}"
                >

                <div class="card-content">

                    <div class="hotel-rating">
                        ⭐ ${hotel.rating}
                    </div>
                <h3 data-key="${hotel.name.replaceAll(' ','')}">
               ${hotel.name}
                </h3>

                  <p class="hotel-location" data-key="${hotel.city}">
                 📍 ${hotel.city}
                </p>
                <p data-key="${hotel.name.replaceAll(' ','')}Desc">
                 ${hotel.description}
                 </p>
                
                    <p>
                        🛏️ Rooms:
                        ${hotel.rooms_available}
                    </p>

                    <div class="hotel-features">

                        ${hotel.wifi
                        ? "<span>📶 WiFi</span>"
                        : ""}

                        ${hotel.pool
                        ? "<span>🏊 Pool</span>"
                        : ""}

                        ${hotel.spa
                        ? "<span>💆 Spa</span>"
                        : ""}

                        ${hotel.restaurant
                        ? "<span>🍽 Restaurant</span>"
                        : ""}

                    </div>

                    <div class="hotel-footer">

                        <div class="price">

                            ${hotel.price}
                            MAD

                        </div>

                        <button
                        class="reserve-btn"
                        onclick="openReservation('${hotel.name}')">

                            Reserve

                        </button>

                    </div>

                </div>

            </div>

            `;

        });

        activateSearch();

applyLanguage(
document.getElementById("language").value
);

    }

    catch(error){

        console.error(error);

    }

}


/* Search Hotels */
function activateSearch() {

    const searchInput =
        document.getElementById(
            "searchHotel"
        );

    if(!searchInput) return;

    searchInput.addEventListener(
        "keyup",
        function(){

        const value =
            this.value.toLowerCase();

        const cards =
            document.querySelectorAll(
                ".hotel-card"
            );

        cards.forEach(card => {

            const text =
                card.textContent
                .toLowerCase();

            card.style.display =
                text.includes(value)
                ? "block"
                : "none";

        });

    });

}


/* Reservation */
async function reserveHotel() {

    const full_name =
        document.getElementById(
            "fullname"
        ).value;

    const email =
        document.getElementById(
            "email"
        ).value;

    const hotel_name =
        document.getElementById(
            "hotel"
        ).value;

    const check_in =
        document.getElementById(
            "checkin"
        ).value;

    const check_out =
        document.getElementById(
            "checkout"
        ).value;

    const guests =
        document.getElementById(
            "guests"
        ).value;

    if(
        !full_name ||
        !email ||
        !hotel_name ||
        !check_in ||
        !check_out ||
        !guests
    ){

        alert(
            "Fill all fields"
        );

        return;
    }

    try {

        const response =
            await fetch(
                "http://127.0.0.1:5000/reserve",
                {
                    method:"POST",

                    headers:{
                        "Content-Type":
                        "application/json"
                    },

                    body:
                    JSON.stringify({

                        full_name,
                        email,
                        hotel_name,
                        check_in,
                        check_out,
                        guests

                    })

                }
            );

const result =
    await response.json();

document.getElementById(
    "reservationMessage"
).innerHTML = `

<div style="
background:#d4edda;
color:#155724;
padding:15px;
border-radius:10px;
margin-bottom:20px;
font-weight:bold;
">

✅ Reservation Confirmed

<br><br>

📧 ${result.message}

</div>

<h2>Invoice</h2>

<p>
<b>Client:</b>
${result.customer}
</p>

<p>
<b>Hotel:</b>
${result.hotel}
</p>

<p>
<b>Check In:</b>
${result.check_in}
</p>

<p>
<b>Check Out:</b>
${result.check_out}
</p>

<p>
<b>Guests:</b>
${result.guests}
</p>

<p>
<b>Total:</b>
${result.total} MAD
</p>

`;

  }
        
    catch(error){

        console.error(error);

        alert(
            "Server Error"
        );

    }

}


/* Open Reservation */
function openReservation(hotelName){

    document
    .getElementById("hotel")
    .value = hotelName;

    document
    .getElementById("reservation")
    .scrollIntoView({

        behavior:"smooth"

    });

}


/* Favorites */
async function toggleFavorite(el, hotelName){

    el.classList.toggle("active");

    const userEmail =
        localStorage.getItem("user_email");

 

    try{

        await fetch(
            "http://127.0.0.1:5000/favorite",
            {
                method:"POST",

                headers:{
                    "Content-Type":
                    "application/json"
                },

                body:JSON.stringify({

                    user_email:userEmail,
                    hotel_name:hotelName

                })

            }
        );

    }

    catch(error){

        console.error(error);

    }

}

/* Reviews */
async function addReview(){

    const name =
        document.getElementById("reviewName").value;

    const hotel =
        document.getElementById("reviewHotel").value;

    const stars =
        document.getElementById("reviewStars").value;

    const text =
        document.getElementById("reviewText").value;

    if(!name || !text){

        alert("Fill all fields");
        return;

    }

    try{

        const response =
            await fetch(
                "http://127.0.0.1:5000/review",
                {
                    method:"POST",

                    headers:{
                        "Content-Type":
                        "application/json"
                    },

                    body:JSON.stringify({

                        name:name,
                        hotel_name:hotel,
                        rating:stars,
                        comment:text

                    })

                }
            );

        const result =
            await response.json();

        if(result.success){

            document.getElementById(
                "reviewsContainer"
            ).innerHTML += `

            <div class="card">

                <div class="card-content">

                    <h3>${name}</h3>

                    <p>🏨 ${hotel}</p>

                    <p>${"⭐".repeat(stars)}</p>

                    <p>${text}</p>

                </div>

            </div>

            `;

           

            document.getElementById(
                "reviewName"
            ).value = "";

            document.getElementById(
                "reviewText"
            ).value = "";

        }

    }

    catch(error){

        console.error(error);

        alert("Server Error");

    }

}


/* LOGIN */
async function login() {

    const email =
        document.getElementById("email").value;

    const password =
        document.getElementById("password").value;

    if (
        !email ||
        !password
    ) {

        alert("Fill all fields");
        return;

    }

    try {

        const response =
            await fetch(
                "http://127.0.0.1:5000/login",
                {
                    method: "POST",

                    headers: {
                        "Content-Type":
                        "application/json"
                    },

                    body: JSON.stringify({

                        email,
                        password

                    })

                }
            );

        const result =
            await response.json();

        alert(result.message);

        if (result.success) {

            localStorage.setItem(
                "user_email",
                email
            );

            window.location.href =
                "index.html";

        }

    }

    catch (error) {

        console.error(error);

        alert("Server Error");

    }

}

const translations = {

  English: {

    heroTitle: "Discover Morocco",
    heroText: "Explore magical destinations, luxury hotels and unforgettable experiences.",
    exploreBtn: "Explore Now",
    destinationsTitle: "Top Destinations",

    marrakechTitle: "Marrakech",
    marrakechText: "Discover the beauty of Marrakech with luxury riads and magical souks.",

    chefchaouenTitle: "Chefchaouen",
    chefchaouenText: "The blue pearl of Morocco with incredible mountain views.",

    saharaTitle: "Sahara",
    saharaText: "Enjoy unforgettable nights under the stars in the Moroccan desert.",

    taghazoutTitle: "Taghazout",
    taghazoutText: "Taghazout, pearl of the Moroccan Atlantic coast, where the ocean meets the serenity of the mountains and the spirit of surfing",

    agadirTitle: "Agadir",
    agadirText: "Agadir is the seaside pearl of southern Morocco: a modern and dynamic city bathed in sun all year round, famous for its large cornice, its impressive fortress of Agadir Oufella and its long golden sand beaches",

    marrakechTitle1: "Marrakech",
    marrakechText1: "The Koutoubia Mosque is the largest religious building and emblematic symbol of Marrakech. Its minaret rises to nearly 77 meters.",

    casablancaTitle: "Casablanca",
    casablancaText: "Economic capital of Morocco and one of the largest cities in North Africa.",

    fezTitle1: "Fez",
    fezText1: "Lamps, Medina of Fez.",

    fezTitle: "Fez",
    fezText: "Fez is the spiritual and cultural capital of Morocco.",

    amazighTitle: "Amazigh",
    amazighText: "The Amazighs are the indigenous people of North Africa and an essential part of Morocco's identity.",

    nadorTitle: "Nador",
    nadorText: "Nador is a large coastal city in northeastern Morocco, famous for Mar Chica lagoon."
  },

  Français: {

    heroTitle: "Découvrir le Maroc",
    heroText: "Explorez des destinations magiques, des hôtels de luxe et des expériences inoubliables.",
    exploreBtn: "Explorer",
    destinationsTitle: "Destinations Populaires",

    marrakechTitle: "Marrakech",
    marrakechText: "Découvrez la beauté de Marrakech avec ses riads luxueux et ses souks magiques.",

    chefchaouenTitle: "Chefchaouen",
    chefchaouenText: "La perle bleue du Maroc avec des vues montagneuses incroyables.",

    saharaTitle: "Sahara",
    saharaText: "Profitez de nuits inoubliables sous les étoiles du désert marocain.",

    taghazoutTitle: "Taghazout",
    taghazoutText: "Perle de la côte atlantique marocaine où l'océan rencontre la sérénité des montagnes.",

    agadirTitle: "Agadir",
    agadirText: "Agadir est la perle balnéaire du sud du Maroc, connue pour ses plages dorées.",

    marrakechTitle1: "Marrakech",
    marrakechText1: "La mosquée Koutoubia est le symbole emblématique de Marrakech.",

    casablancaTitle: "Casablanca",
    casablancaText: "Capitale économique du Maroc et l'une des plus grandes villes du Maghreb.",

    fezTitle1: "Fès",
    fezText1: "Lampes, médina de Fès.",

    fezTitle: "Fès",
    fezText: "Fès est la capitale spirituelle et culturelle du Maroc.",

    amazighTitle: "Amazigh",
    amazighText: "Les Amazighs sont les peuples autochtones de l'Afrique du Nord.",

    nadorTitle: "Nador",
    nadorText: "Nador est une grande ville côtière du nord-est du Maroc."
  },

  العربية: {

    heroTitle: "اكتشف المغرب",
    heroText: "استكشف وجهات ساحرة وفنادق فاخرة وتجارب لا تنسى.",
    exploreBtn: "استكشف الآن",
    destinationsTitle: "أفضل الوجهات",

    marrakechTitle: "مراكش",
    marrakechText: "اكتشف جمال مراكش برياضاتها الفاخرة وأسواقها التقليدية.",

    chefchaouenTitle: "شفشاون",
    chefchaouenText: "اللؤلؤة الزرقاء للمغرب بإطلالات جبلية رائعة.",

    saharaTitle: "الصحراء",
    saharaText: "استمتع بليالٍ لا تنسى تحت نجوم الصحراء المغربية.",

    taghazoutTitle: "تغازوت",
    taghazoutText: "لؤلؤة الساحل الأطلسي المغربي حيث يلتقي المحيط بسحر الجبال.",

    agadirTitle: "أكادير",
    agadirText: "أكادير جوهرة الجنوب المغربي المشهورة بشواطئها الذهبية.",

    marrakechTitle1: "مراكش",
    marrakechText1: "مسجد الكتبية هو الرمز التاريخي والأشهر لمدينة مراكش.",

    casablancaTitle: "الدار البيضاء",
    casablancaText: "العاصمة الاقتصادية للمغرب وإحدى أكبر مدن شمال إفريقيا.",

    fezTitle1: "فاس",
    fezText1: "مصابيح المدينة العتيقة بفاس.",

    fezTitle: "فاس",
    fezText: "فاس هي العاصمة الروحية والثقافية للمغرب.",

    amazighTitle: "الأمازيغ",
    amazighText: "الأمازيغ هم السكان الأصليون لشمال إفريقيا وجزء أساسي من هوية المغرب.",

    nadorTitle: "الناظور",
    nadorText: "الناظور مدينة ساحلية كبيرة تقع شمال شرق المغرب."
  }
};


document.getElementById("language").addEventListener("change", function () {

  const lang = this.value;

  document.getElementById("hero-title").innerText =
      translations[lang].heroTitle;

  document.getElementById("hero-text").innerText =
      translations[lang].heroText;

  document.getElementById("explore-btn").innerText =
      translations[lang].exploreBtn;

  document.getElementById("destinations-title").innerText =
      translations[lang].destinationsTitle;

  document.querySelectorAll("[data-key]").forEach(el => {

      const key = el.dataset.key;

      if (translations[lang][key]) {

          el.innerText =
              translations[lang][key];

      }

  });

});

function applyLanguage(lang){

document
.querySelectorAll("[data-key]")
.forEach(element => {

const key =
element.getAttribute("data-key");

if(
translations[lang] &&
translations[lang][key]
){
element.textContent =
translations[lang][key];
}

if(
hotelTranslations[lang] &&
hotelTranslations[lang][key]
){
element.textContent =
hotelTranslations[lang][key];
}

});

}


   



const hotelTranslations = {

English: {

LaMamounia: "La Mamounia",
LaMamouniaDesc: "Luxury palace hotel in Marrakech",

FairmontTaghazoutBay: "Fairmont Taghazout Bay",
FairmontTaghazoutBayDesc: "Luxury resort facing Atlantic Ocean",

SofitelAgadirRoyalBay: "Sofitel Agadir Royal Bay",
SofitelAgadirRoyalBayDesc: "Luxury seaside hotel",

MazaganBeachResort: "Mazagan Beach Resort",
MazaganBeachResortDesc: "Luxury beach resort with golf course, spa and ocean views.",

RiadFes: "Riad Fes",
RiadFesDesc: "Traditional luxury riad located in the historic medina of Fez.",

RoyalMansour: "Royal Mansour",
RoyalMansourDesc: "One of the most luxurious hotels in Morocco with private riads.",

FourSeasonsResort: "Four Seasons Resort",
FourSeasonsResortDesc: "Luxury resort with gardens, pools and premium services.",

ParadisPlageResort: "Paradis Plage Resort",
ParadisPlageResortDesc: "Beachfront eco-resort famous for surfing and wellness.",

BanyanTreeTamoudaBay: "Banyan Tree Tamouda Bay",
BanyanTreeTamoudaBayDesc: "Luxury villas with private pools on the Mediterranean coast.",

RadissonBluResort: "Radisson Blu Resort",
RadissonBluResortDesc: "Modern seaside resort with family activities and pools.",

HiltonTangierAlHouara: "Hilton Tangier Al Houara",
HiltonTangierAlHouaraDesc: "Luxury hotel with golf course and Atlantic Ocean views.",

TheViewHotel: "The View Hotel",
TheViewHotelDesc: "Modern luxury hotel located in the heart of Rabat.",

BeLiveCollection: "Be Live Collection",
BeLiveCollectionDesc: "All-inclusive beachfront hotel with luxury facilities."

},

Français: {

LaMamounia: "La Mamounia",
LaMamouniaDesc: "Palace hôtel de luxe à Marrakech",

FairmontTaghazoutBay: "Fairmont Taghazout Bay",
FairmontTaghazoutBayDesc: "Complexe de luxe face à l'océan Atlantique",

SofitelAgadirRoyalBay: "Sofitel Agadir Royal Bay",
SofitelAgadirRoyalBayDesc: "Hôtel de luxe en bord de mer",

MazaganBeachResort: "Mazagan Beach Resort",
MazaganBeachResortDesc: "Resort balnéaire de luxe avec golf, spa et vue sur l'océan",

RiadFes: "Riad Fès",
RiadFesDesc: "Riad traditionnel de luxe situé dans la médina historique de Fès",

RoyalMansour: "Royal Mansour",
RoyalMansourDesc: "L'un des hôtels les plus luxueux du Maroc avec riads privés",

FourSeasonsResort: "Four Seasons Resort",
FourSeasonsResortDesc: "Resort de luxe avec jardins, piscines et services haut de gamme",

ParadisPlageResort: "Paradis Plage Resort",
ParadisPlageResortDesc: "Éco-resort en bord de mer célèbre pour le surf et le bien-être",

BanyanTreeTamoudaBay: "Banyan Tree Tamouda Bay",
BanyanTreeTamoudaBayDesc: "Villas de luxe avec piscines privées sur la côte méditerranéenne",

RadissonBluResort: "Radisson Blu Resort",
RadissonBluResortDesc: "Complexe balnéaire moderne avec activités familiales",

HiltonTangierAlHouara: "Hilton Tangier Al Houara",
HiltonTangierAlHouaraDesc: "Hôtel de luxe avec golf et vue sur l'Atlantique",

TheViewHotel: "The View Hotel",
TheViewHotelDesc: "Hôtel de luxe moderne au cœur de Rabat",

BeLiveCollection: "Be Live Collection",
BeLiveCollectionDesc: "Hôtel tout compris en bord de mer avec équipements de luxe"

},

العربية: {

LaMamounia: "لا مامونية",
LaMamouniaDesc: "قصر فندقي فاخر بمدينة مراكش",

FairmontTaghazoutBay: "فيرمونت تغازوت باي",
FairmontTaghazoutBayDesc: "منتجع فاخر يطل على المحيط الأطلسي",

SofitelAgadirRoyalBay: "سوفيتيل أكادير رويال باي",
SofitelAgadirRoyalBayDesc: "فندق فاخر على شاطئ البحر",

MazaganBeachResort: "منتجع مازاغان",
MazaganBeachResortDesc: "منتجع شاطئي فاخر يضم ملعب غولف ومنتجعاً صحياً وإطلالة بحرية",

RiadFes: "رياض فاس",
RiadFesDesc: "رياض فاخر تقليدي داخل المدينة العتيقة لفاس",

RoyalMansour: "رويال منصور",
RoyalMansourDesc: "من أفخم فنادق المغرب ويضم رياضات خاصة",

FourSeasonsResort: "فور سيزونز",
FourSeasonsResortDesc: "منتجع فاخر بحدائق ومسابح وخدمات مميزة",

ParadisPlageResort: "باراديس بلاج",
ParadisPlageResortDesc: "منتجع بيئي على البحر مشهور برياضة ركوب الأمواج والاسترخاء",

BanyanTreeTamoudaBay: "بانيان تري تمودا باي",
BanyanTreeTamoudaBayDesc: "فلل فاخرة بمسابح خاصة على الساحل المتوسطي",

RadissonBluResort: "راديسون بلو",
RadissonBluResortDesc: "منتجع عصري على البحر مع أنشطة عائلية",

HiltonTangierAlHouara: "هيلتون طنجة الهوارة",
HiltonTangierAlHouaraDesc: "فندق فاخر مع ملعب غولف وإطلالة على المحيط الأطلسي",

TheViewHotel: "ذا فيو",
TheViewHotelDesc: "فندق عصري فاخر في قلب الرباط",

BeLiveCollection: "بي لايف كولكشن",
BeLiveCollectionDesc: "فندق شامل الخدمات على الشاطئ بمرافق فاخرة"

},


      }




  function convertCurrency() {

    const mad =
        parseFloat(
            document.getElementById(
                "madInput"
            ).value
        );

    if(isNaN(mad)){

        alert(
            "Enter a valid amount"
        );

        return;
    }

    const usd =
        (mad / 10).toFixed(2);

    const eur =
        (mad / 11).toFixed(2);

    document.getElementById(
        "result"
    ).innerHTML = `

         USD : ${usd}<br>
         EUR : ${eur}

    `;
}    




window.onload = () => {

    loadHotels();

    const languageSelect =
        document.getElementById("language");

    languageSelect.addEventListener(
        "change",
        function () {

            applyLanguage(
                this.value
            );

        }
    );

};
