top_albuns = ['twenty one pilots', 'regional at best', 'vessel', 'blurryface', 'trench', 'scaled and icy', 'clancy'];
while True:
    fav_album = input("What's your favorite twenty one pilots album? ")
    if fav_album in top_albuns:
     if fav_album == "twenty one pilots":
        print("No way! That's my favorite too! Nice choice.")
        break
     else:
         print(f"Very nice! {fav_album.title()} is a great choice. My favorite album is {top_albuns[0]}.")
         break
    else:
        print("I don't know that one, but I bet it's a good one.")
        