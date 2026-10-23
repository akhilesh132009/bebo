#include <iostream>
#include <vector>
#include <string>
#include <cstdlib>
#include <ctime>

using namespace std;

int main() {
    vector<string> messages = {
        "Anjali, you make my world beautiful! <3",
        "Bebo, you are my favourite person! <3",
        "Every star reminds me of your smile!",
        "Sending you a thousand virtual hugs!",
        "With love, your Akhilesh!"
    };

    srand(static_cast<unsigned int>(time(nullptr)));

    int choice = rand() % messages.size();

    cout << messages[choice] << endl;

    return 0;
}#include <iostream>
#include <vector>
#include <string>
#include <random>

int main() {
    const std::vector<std::string> messages = {
        "Bebo, tumhari smile kisi bhi din ko special bana sakti hai. <3",
        "Universe mein stars bahut hain, par tumhari vibe alag hai.",
        "Bebo, keep shining. You deserve all the beautiful things in this universe.",
        "A little reminder from Akhilesh: keep smiling and take care of yourself.",
        "Aaj ka mission: smile karna aur khud ka khayal rakhna."
    };

    std::random_device rd;
    std::mt19937 gen(rd());

    std::uniform_int_distribution<std::size_t> dist(
        0, messages.size() - 1
    );

    std::cout << messages[dist(gen)] << '\n';

    return 0;
}
