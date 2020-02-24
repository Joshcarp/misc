package main

import (
	"encoding/base64"
	"encoding/json"
	"fmt"
	"io/ioutil"
	"os"
)

const command = `grpcurl -v -H "Authorization: Basic %s"  <ServiceURL here> <Method invocation here>`

func main() {
	var info map[string]map[string]string
	if len(os.Args) < 2 {
		fmt.Println("Please specify an input file")
		os.Exit(1)
	}

	dat, err := ioutil.ReadFile(os.Args[1])
	if err != nil {
		panic(err)
	}
	json.Unmarshal(dat, &info)
	for _, val := range info {
		encoded := Encode(val["username"] + ":" + val["password"])
		finishedCommand := fmt.Sprintf(command, encoded)
		fmt.Println(finishedCommand)
	}
}

func Encode(str string) string {
	return base64.StdEncoding.EncodeToString([]byte(str))
}
