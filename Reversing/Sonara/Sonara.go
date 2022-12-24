package main

import "fmt"

// ##################
// Author => IronByte
// ##################

func welcome() {
	fmt.Printf("################################### \n")
	fmt.Printf("############# SONARA ############## \n")
	fmt.Printf("################################### \n")
}

func win() {
	fmt.Printf("Good Job that's the right flag ! \n")
	fmt.Printf("For more follow me on ironbyte.me ! \n ")
}

func fail() {
	fmt.Print("Sonara SHUTDOWN NOW ! \n")
}

func main() {
	welcome()
	fmt.Printf("Flag : ")
	var flag string
	fmt.Scanln(&flag)
	chars := []rune(flag)

	enc_flag := ([]byte{166, 202, 198, 234, 228, 210, 220, 202, 232, 230, 246, 110, 208, 102, 242, 190, 106, 104, 242, 190, 114, 96, 190, 98, 106, 190, 110, 208, 102, 190, 204, 234, 110, 234, 100, 102, 66, 250})
	gen_flag := ""
	for i := 0; i < len(chars); i++ {
		ascii := int(chars[i])
		if i%2 == 1 {
			c := string(rune(ascii << 1))
			gen_flag += c
		} else {
			c := string(rune(ascii * 2))
			gen_flag += c
		}
	}

	iter := []rune(gen_flag)

	for i := 0; i < len(iter); i++ {
		if iter[i] != rune(enc_flag[i]) {
			fail()
			return
		}
	}
	win()

}
