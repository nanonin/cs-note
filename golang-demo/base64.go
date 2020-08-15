package main

import (
    "encoding/base64"
    "fmt"
    "log"
    "flag"
)

func main() {
    var mode string
    var str string
    flag.StringVar(&mode, "m", "0", "模式,默认为加密 ")
    flag.StringVar(&str, "t", "", "输入字符,默认为空")
    //这里有一个非常重要的操作,转换， 必须调用该方法
    flag.Parse()

    //输出结果
    // fmt.Printf("mode=%v str=%v", mode, str)
    if mode == "0" && str != "" {
        fmt.Printf("Base64Encode res:%v ", base64Encode(str))
        return
    } else if mode != "0" && str != "" {
        fmt.Printf("Base64Decode res:%v ", base64Decode(str))
        return
    } else if str == "" {
        fmt.Printf("params str is null")
        return
    }
}

func base64urlEncode(str string) string {
    input := []byte(str)
    uEnc := base64.URLEncoding.EncodeToString([]byte(input))
    return uEnc
}

func basse64urlDecode(uEnc string) string {
    uDec, err := base64.URLEncoding.DecodeString(uEnc)
    if err != nil {
        log.Fatalln(err)
    }
    return string(uDec)
}

func base64Encode(str string) string {
     input := []byte(str)
     encodeString := base64.StdEncoding.EncodeToString(input)
     return encodeString
}

func base64Decode(encodeString string) string {
    decodeBytes, err := base64.StdEncoding.DecodeString(encodeString)
    if err != nil {
            log.Fatalln(err)
    }
    return string(decodeBytes)
}