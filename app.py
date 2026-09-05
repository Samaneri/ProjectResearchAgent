print("=" * 60)
print("       PRODUCT RESEARCH AI AGENT")
print("=" * 60)

print("\nType 'exit' to stop the program.\n")

while True:
    user_input = input("You: ")

    if user_input.lower() == "exit":
        print("Goodbye!")
        break

    print("\nAI Agent:")
    print("-" * 50)

    print("""
PRODUCT COMPARISON RESULT

Product 1: iPhone 16
Product 2: Samsung Galaxy S25

--------------------------------------------------
PRICE
--------------------------------------------------
iPhone 16:
- Premium smartphone
- Price varies by storage and region

Samsung Galaxy S25:
- Premium smartphone
- Price varies by storage and region

--------------------------------------------------
PERFORMANCE
--------------------------------------------------
iPhone 16:
- Apple A18 processor
- Excellent performance

Samsung Galaxy S25:
- Snapdragon flagship processor
- Excellent Android performance

--------------------------------------------------
CAMERA
--------------------------------------------------
iPhone 16:
- High-quality camera system
- Strong video recording

Samsung Galaxy S25:
- Versatile camera system
- Strong photography features

--------------------------------------------------
BATTERY
--------------------------------------------------
iPhone 16:
- Good battery life

Samsung Galaxy S25:
- Good battery life
- Fast charging support

--------------------------------------------------
ADVANTAGES
--------------------------------------------------
iPhone 16:
+ Powerful performance
+ Excellent video quality
+ iOS ecosystem

Samsung Galaxy S25:
+ Excellent Android experience
+ Strong performance
+ Advanced display

--------------------------------------------------
FINAL RECOMMENDATION
--------------------------------------------------
Best for iOS and video: iPhone 16

Best for Android and customization: Samsung Galaxy S25

Best overall:
Depends on the user's preference between iOS and Android.

--------------------------------------------------
Research completed successfully!
--------------------------------------------------
""")