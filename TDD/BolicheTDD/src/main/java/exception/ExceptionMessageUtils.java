package exception;

import java.io.IOException;
import java.io.InputStream;
import java.util.Properties;

public class ExceptionMessageUtils {

    // Método que retorna a mensagem de erro correspondente a uma determinada chave.
    // Utiliza um arquivo .properties chamado "error_messages.properties" para armaz
    // enar as mensagens de erro. O método carrega esse arquivo e retorna a mensagem
    // correspondente à chave fornecida como parâmetro. Se o arquivo não for encontra
    // do, o método retorna null.

    public static String getMessage(String key) {
        Properties properties = new Properties();
        InputStream inputStream = ExceptionMessageUtils.class.getClassLoader().getResourceAsStream("error_messages.properties");
        if (inputStream != null) {
            try {
                properties.load(inputStream);
            } catch (IOException e) {
                throw new RuntimeException(e);
            }
            return properties.getProperty(key);
        }
        return null;
    }

}
