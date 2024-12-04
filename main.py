from fasthtml.common import *
from fastapi.staticfiles import StaticFiles
from styles import styles
from cards import MENTOR_CARDS

app, rt = fast_app()

# Serve static files
app.mount("/img", StaticFiles(directory="img"), name="img")
app.mount("/pdf", StaticFiles(directory="pdf"), name="pdf")

def render_head(title):
    """Render the <head> section with dynamic title and favicon."""
    return Head(
        Title(title),
        Link(rel="icon", href="/img/favicon.ico?v=2"),
        Meta(charset="UTF-8"),
        Meta(name="viewport", content="width=device-width, initial-scale=1.0"),
    )

def render_footer():
    """Render the footer section."""
    return Div(
        Div(
            Div(
                P(
                    "A project by ",
                    A("Illawarra Multicultural Services", href="https://ims.org.au/", target="_blank"),
                ),
                _style="text-align: center; margin: 10px 0;"
            ),
            Div(
                P(
                    "Web Development by ",
                    A("Code.Sydney", href="https://www.code.sydney/", target="_blank"),
                ),
                P("© 2025 Illawarra Multicultural Services. All rights reserved."),
                _style="text-align: center; margin: 10px 0; font-size: small; color: gray;"
            ),
            _style="background-color: #f8f9fa; padding: 20px; border-top: 1px solid #ddd;"
        )
    )

def render_header():
    """Render the consistent header across pages."""
    return Div(
        Div(
            A(
                Img(src="/img/migramlogo.png", alt="IMS Logo", _style="width: 225px; margin-bottom: 10px;"),
                _style="text-align: center;",
                href="https://www.migram.au"
            )
        ),        
        #H1("MIGRAM", _style="text-align: center; margin-bottom: 10px; font-size: 3rem;"),
        P("Empowering migrants of refugee background to thrive and build inclusive communities.", _style="text-align: center; margin-bottom: 10px;"),
        Div(
            A(
                Img(src="/img/imslogo.png", alt="IMS Logo", _style="width: 300px; margin-bottom: 10px;"),
                _style="text-align: center;",
                href="https://ims.org.au/",
                target="_blank"
            )
        ),
        _style="text-align: center; font-family: Arial, sans-serif;"
    )

def render_page(custom_body):
    """Render a page with a consistent header and dynamic body."""
    return Body(
        Div(
            styles,
            render_header(),
            custom_body,
            Div(
                Div(
                    Img(src="img/Farhan.png", alt="My Story Image", _style="width: 100%;"),
                    P(
                        "This is the story of how I became a mentor...",
                        _style="text-align: center; margin: 20px; font-size: 18px;"
                    ),
                    A(
                        "Close",
                        href="#",
                        _class="close-modal",
                        _style="display: block; text-align: center; margin-top: 20px; color: red;"
                    ),
                    _class="modal-content",
                ),
                _id="my-story-modal",
                _class="modal",
            )
        ),
        _style="font-family: Arial, sans-serif; margin: 40px;"
    )

def render_navbar():
    """Render the burger menu for navigation."""
    return Div(
        Div(
            Div("☰", _class="burger-icon"),
            Div(
                A("Home", href="/", _class="menu-item", _style="display: block; padding: 10px 20px; font-family: Arial;"),
                A("About", href="/about", _class="menu-item", _style="display: block; padding: 10px 20px; font-family: Arial;"),
                _class="menu-content",
                _style="display: none; position: absolute; top: 40px; right: 0; background-color: white; box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.1); z-index: 999;"
            ),
            _style="position: relative;"
        ),
        Script("""
        const burgerIcon = document.querySelector('.burger-icon');
        const menuContent = document.querySelector('.menu-content');

        burgerIcon.addEventListener('click', () => {
            menuContent.style.display = menuContent.style.display === 'block' ? 'none' : 'block';
        });

        window.addEventListener('click', (event) => {
            if (!event.target.matches('.burger-icon')) {
                menuContent.style.display = 'none';
            }
        });
        """),
        _style="position: fixed; top: 10px; right: 10px; padding: 10px; background-color: #f8f9fa; border-radius: 5px; box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.1); z-index: 1000;"
    )

@rt("/")
def get(req):
    return Html(
        render_head("Migram - Home"),
        render_navbar(),
        render_page(
            Div(
                Div(
                    Input(_type="text", _placeholder="Search service providers...", _id="search-input", _style="padding: 10px; width: 300px;"),
                    _style="text-align: center; margin: 20px;"
                ),
                Div(
                    *MENTOR_CARDS,
                    _id="portfolio-container",
                    _style="display: flex; flex-wrap: wrap; justify-content: center;"
                ),
                Script("""
                document.getElementById('search-input').addEventListener('input', function() {
                    const query = this.value.toLowerCase();
                    const cards = document.querySelectorAll('.card');

                    cards.forEach(card => {
                        const title = card.querySelector('.card-title').textContent.toLowerCase();
                        const description = card.querySelector('.card-description').textContent.toLowerCase();
                        const isMatch = title.includes(query) || description.includes(query);
                        card.style.display = isMatch ? 'block' : 'none';
                    });
                });
                """),
            )
        ),
        render_footer()
    )

@rt("/about")
def about(req):
    return Html(
        render_head("Migram - About"),
        render_navbar(),
        render_page(
            Div(
                H2("About Us", _style="text-align: center; margin-bottom: 20px;"),
                P(
                    "Migram is a dedicated platform designed to connect migrants from refugee backgrounds with opportunities for low-skilled work. The aim is to help them integrate into their local communities, fostering meaningful connections and participation. At the same time, Migram serves as a way for local communities to support these individuals, creating a network of mutual benefit and empowerment. By bridging the gap, Migram not only provides economic opportunities but also builds a foundation for stronger, more inclusive communities.",
                    _style="text-align: center; font-family: Arial, sans-serif; margin: 20px;"
                ),
            )
        ),
        render_footer()
    )

@rt("/my-story-farhan")
def my_story_farhan(req):
    return Html(
        render_head("Farhan’s Journey: From Tragedy to Triumph"),
        render_navbar(),
        render_page(
            Div(
                H2("Farhan’s Journey: From Tragedy to Triumph", _style="text-align: center; margin-bottom: 20px;"),
                P(
                    """Farhan was born in Afghanistan in 1997, a year marked by tragedy. His mother passed away while 
                    giving birth to him, and at the age of two, he lost his father, who was killed by the Taliban. 
                    With both parents gone, Farhan's uncle took him to Pakistan, raising him as his own child. For years, 
                    Farhan believed that his uncle and his uncle’s wife were his biological parents.""",
                    _style="text-align: justify; margin: 20px;"
                ),
                P(
                    """Growing up in Pakistan, Farhan excelled in his studies, learning both English and computer skills. 
                    In 2010, his uncle made the dangerous journey to Australia by boat, seeking a better life. Two years later, 
                    in 2012, Farhan’s uncle began the process of bringing the rest of the family to Australia. The family went 
                    to the Australian Embassy in Islamabad, Pakistan, where they underwent a DNA test as part of the visa process.""",
                    _style="text-align: justify; margin: 20px;"
                ),
                P(
                    """It was during this test that Farhan’s life took an unexpected turn. The results revealed that he was not 
                    biologically related to the family he had always believed was his own. It was then that Farhan learned the 
                    painful truth—his father had been his uncle all along. This revelation shattered his world.""",
                    _style="text-align: justify; margin: 20px;"
                ),
                P(
                    """From that point on, Farhan remained in Pakistan, living with his aunt. In 2013, when the wave of violence 
                    against Hazaras escalated in Pakistan, Farhan had no choice but to flee. His journey took him to Thailand, 
                    then Malaysia, and finally to Indonesia in 2014. Smuggled into Indonesia, Farhan registered with the United 
                    Nations High Commissioner for Refugees (UNHCR) as an asylum seeker.""",
                    _style="text-align: justify; margin: 20px;"
                ),
                P(
                    """For 21 months, Farhan was held in a detention centre in the Indonesian city of Tanjungpinang, where he 
                    used his English skills to assist the UNHCR as a translator. In time, his asylum status was changed to that 
                    of a refugee, and he was moved to the city of Batam, where he shared a room with another refugee. Farhan spent 
                    nearly three years in Batam before being sent back to Tanjungpinang, where he lived from 2018 until 2022.""",
                    _style="text-align: justify; margin: 20px;"
                ),
                P(
                    """During these difficult years, Farhan learned Bahasa Indonesia and continued helping the UNHCR with 
                    translation work. His uncle in Australia supported him financially, ensuring that Farhan could survive in 
                    Indonesia. In 2022, his uncle initiated the process of bringing Farhan to Australia through the Community 
                    Support Program (CSP).""",
                    _style="text-align: justify; margin: 20px;"
                ),
                P(
                    """In September 2023, after years of hardship and displacement, Farhan finally arrived in Australia.""",
                    _style="text-align: justify; margin: 20px;"
                ),
                P(
                    """ "Since I arrived in Australia, I feel like I was born again," Farhan says. He has already obtained his 
                    driver’s license in Sydney and found work as a house painter. Farhan is deeply grateful for the peace and 
                    security he has found after years of turmoil. "I owe a lot to Australia for the peaceful life I have now, 
                    after all these years of struggle." """,
                    _style="text-align: justify; margin: 20px;"
                ),
                P(
                    """Farhan’s story is one of resilience, courage, and hope—a testament to the strength of the human spirit in 
                    the face of unimaginable adversity, and to the transformative power of programs like CSP that enable refugees 
                    to find peace and opportunity in Australia.""",
                    _style="text-align: justify; margin: 20px;"
                ),
                A(
                    "Back to Home",
                    href="/",
                    _style="display: block; text-align: center; margin-top: 20px; color: blue; text-decoration: underline;"
                )
            )
        ),
        render_footer()
    )

serve()
