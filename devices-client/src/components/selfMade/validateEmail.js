const validateEmail = (value) => {
    if (value == []) {
        console.log(value);
        return 'メールアドレスを入力してください。';
    }
    return undefined;
}

export default validateEmail;