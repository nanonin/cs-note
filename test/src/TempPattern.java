public class TempPattern {

    public static void main(String[] args) {
        MyPagerTemplate t1 = new MyPagerTemplate() {
            @Override
            String head() {
                return "H1";
            }

            @Override
            String title() {
                return "T1";
            }

            @Override
            String content() {
                return "hello world";
            }
        };
        MyPagerTemplate t2 = new MyPagerTemplate() {
            @Override
            String head() {
                return "H2";
            }

            @Override
            String title() {
                return "T2";
            }

            @Override
            String content() {
                return "fuck world ";
            }
        };

        t1.render();
        t2.render();

    }
}

abstract class MyPagerTemplate {
    abstract String head();

    abstract String title();

    abstract String content();

    public final void render() {
        String sb = "<title>" +
                title() +
                "<title/>" +
                "<head>" +
                head() +
                "<head/>" +
                "<content>" +
                content() +
                "<content/>";
        System.out.println(sb);
    }
}
