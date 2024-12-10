from fasthtml.common import A, Div, H3, Img, P, Style

def generate_my_story_link(story_link, margin_top="0"):
    """Generate a 'My Story' link that redirects to a new page."""
    return A(
        "My Story",
        href=story_link,
        _class="my-story-link",
        style=f"margin-top: {margin_top}; display: block; text-align: center;",
    )

def generate_linkedin_link(linkedin_link, margin_top="0"):
    """Generate LinkedIn link with an icon."""
    return A(
        Img(
            src="img/linkedin-icon.svg",
            alt="LinkedIn",
            _class="linkedin-icon",
            style=f"margin-top: {margin_top};"  # Control the top margin dynamically
        ),
        href=linkedin_link,
        target="_blank",
        _class="linkedin-link"
    )

def generate_portfolio_link(portfolio_link, icon_size=None):
    """Generate portfolio link with a project icon."""
    return A(
        Img(
            src="img/project-icon.png",
            alt="Project",
            _class="portfolio-icon",
            style=f"width: {icon_size}px; height: {icon_size}px;" if icon_size else ""
        ),
        href=portfolio_link,
        target="_blank",
        _class="portfolio-link"
    )

def generate_booking_button(booking_link, margin_bottom="10px"):
    """Generate a booking button with controllable margin."""
    return A(
        "Book Now",
        href=booking_link,
        target="_blank",
        _class="booking-button",
        style=f"margin-bottom: {margin_bottom};"
    )


def card_3d(
    title, background, line1, line2, line3, story_id, show_booking=True, 
    booking_link="", is_portfolio=False, icon_size=None, 
    button_margin_bottom="5px", space_between_button_and_icon="5px"
):
    """Generate a 3D card component with mentor or portfolio details."""
    story_link = f"/story/{story_id}"  # Dynamically generate story link
    card_body = [
        H3(line1, _class="card-title"),  # Mentor name
        P(line2, _class="card-description"),  # Mentor role/description
        A("My Story", href=story_link, _class="my-story-link", _style="margin: 10px 0; text-align: center; display: block;"),
        # P(line3, _class="card-description-small"),  # Additional details
    ]
    if show_booking and not is_portfolio:
        card_body.append(generate_booking_button(booking_link, margin_bottom=button_margin_bottom))

    return Div(
        Div(
            Div(
                _style=f"""
                    background-image: url('{background}');
                    width: 600px;
                    height: 450px;
                """,
                _class="card-image"
            ),
            Div(
                *card_body,
                _class="card-content"
            ),
            _class="card-content",
        ),
        _class="card",
        _style="perspective: 1000px; margin: 20px;",
        _data_title=title,
        _data_description=line1,
        _data_description2=line2
    )


STORIES = {
    "farhan": {
        "title": "Farhan’s Journey: From Tragedy to Triumph",
        "content": """
Farhan was born in Afghanistan in 1997, a year marked by tragedy. His mother passed away while giving birth to him, and at the age of two, he lost his father, who was killed by the Taliban. With both parents gone, Farhan's uncle took him to Pakistan, raising him as his own child. For years, Farhan believed that his uncle and his uncle’s wife were his biological parents.

Growing up in Pakistan, Farhan excelled in his studies, learning both English and computer skills. In 2010, his uncle made the dangerous journey to Australia by boat, seeking a better life. Two years later, in 2012, Farhan’s uncle began the process of bringing the rest of the family to Australia. The family went to the Australian Embassy in Islamabad, Pakistan, where they underwent a DNA test as part of the visa process.

It was during this test that Farhan’s life took an unexpected turn. The results revealed that he was not biologically related to the family he had always believed was his own. It was then that Farhan learned the painful truth—his father had been his uncle all along. This revelation shattered his world.

From that point on, Farhan remained in Pakistan, living with his aunt. In 2013, when the wave of violence against Hazaras escalated in Pakistan, Farhan had no choice but to flee. His journey took him to Thailand, then Malaysia, and finally to Indonesia in 2014. Smuggled into Indonesia, Farhan registered with the United Nations High Commissioner for Refugees (UNHCR) as an asylum seeker.

For 21 months, Farhan was held in a detention centre in the Indonesian city of Tanjungpinang, where he used his English skills to assist the UNHCR as a translator. In time, his asylum status was changed to that of a refugee, and he was moved to the city of Batam, where he shared a room with another refugee. Farhan spent nearly three years in Batam before being sent back to Tanjungpinang, where he lived from 2018 until 2022.

During these difficult years, Farhan learned Bahasa Indonesia and continued helping the UNHCR with translation work. His uncle in Australia supported him financially, ensuring that Farhan could survive in Indonesia. In 2022, his uncle initiated the process of bringing Farhan to Australia through the Community Support Program (CSP).

In September 2023, after years of hardship and displacement, Farhan finally arrived in Australia.

"Since I arrived in Australia, I feel like I was born again," Farhan says. He has already obtained his driver’s license in Sydney and found work as a house painter. Farhan is deeply grateful for the peace and security he has found after years of turmoil. "I owe a lot to Australia for the peaceful life I have now, after all these years of struggle."

Farhan’s story is one of resilience, courage, and hope—a testament to the strength of the human spirit in the face of unimaginable adversity, and to the transformative power of programs like CSP that enable refugees to find peace and opportunity in Australia.


        """
    },
    "waad": {
        "title": "Waad’s Journey: Building Dreams with Carpentry",
        "content": """
        Waad Yousif’s journey is one of resilience, adaptability, and service. Born and raised in Iraq, Waad experienced significant challenges early in life that shaped his determination to create a better future for himself and others. His journey took him from Iraq to Jordan and eventually to Australia, where he now calls Wollongong home.

Waad’s professional career spans multiple industries, reflecting his versatility and strong work ethic. In Iraq, he worked as a sales associate in retail, where he honed his customer service and communication skills. These roles, which ranged from electronics to household goods, taught him the importance of understanding customer needs and providing tailored solutions. After settling in Australia, Waad joined Architectural Hardwood Joinery, where he enhanced his organisational and teamwork skills in a collaborative environment.

Beyond his professional pursuits, Waad is deeply committed to giving back to his community. In Iraq and Jordan, he supported refugees by distributing food and clothing and offering emotional support. In Australia, his volunteer work has continued through roles such as a soccer coach assistant and language interpreter. Fluent in English, Assyrian, and Arabic, Waad uses his language skills to bridge cultural divides and foster inclusivity. He also works with Illawarra Multicultural Services, helping to prepare and deliver meals to students, exemplifying his dedication to community service.

Education has been a cornerstone of Waad’s journey. He has pursued continuous learning, earning a Certificate III in Community Services, completing a Certificate in Spoken and Written English, and participating in leadership training. These achievements highlight his commitment to personal growth and professional development.

Waad’s story is defined by his unwavering perseverance and his ability to connect with others. His experiences have given him a unique perspective on the power of empathy and the importance of community. Today, Waad continues to thrive, inspired by the opportunity to contribute to the vibrant community that has become his home.        
        """
    }
}

MENTOR_CARDS = [
    card_3d(
        "Farhan",
        "img/Farhan.png",
        "Farhan Akhlaqi",
        "Painting Services | ABN 94501731662",  # Mentor role/description
        "",  # Additional info
        story_id="farhan",  # Dynamic story ID
        show_booking=True,
        booking_link="https://ims.org.au/contact-us/",
        button_margin_bottom="1px", 
        space_between_button_and_icon="1px"
    ),
    card_3d(
        "Waad",
        "img/Waad.png",
        "Waad Yousif",
        "Carpentry",  # Mentor role/description
        "",  # Additional info
        story_id="waad",  # Dynamic story ID
        show_booking=True,
        booking_link="https://ims.org.au/contact-us/",
        button_margin_bottom="1px", 
        space_between_button_and_icon="1px"
    )
]    

PORTFOLIO_CARDS = [

]
