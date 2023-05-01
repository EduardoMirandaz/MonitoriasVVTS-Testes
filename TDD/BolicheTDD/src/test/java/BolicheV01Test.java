import boliche.BolicheV01;
import exception.PontuacaoComCaracteresInvalidosException;
import exception.PontuacaoComTamanhoInvalidoException;
import org.junit.jupiter.api.Assertions;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

public class BolicheV01Test {

    BolicheV01 computaPlacarV01;

    @BeforeEach()
    public void setup(){
        computaPlacarV01 = new BolicheV01();
    }

    // --------- [ 01 ] ---------
    @Test
    public void deveRetornarErroCasoAEntradaTenhaUmTamanhoInvalido(){

        String placar = "123";

        Assertions.assertThrows(
                PontuacaoComTamanhoInvalidoException.class,
                () -> computaPlacarV01.computaPlacar(placar)
        );
    }

    // --------- [ 01.1 ] ---------
    // Nessa execução, valido a mensagem de erro, que é uma boa prática
    // tendo em vista que as aplicações devem possuir exceções específicas.
    @Test
    public void deveRetornarErroCasoAEntradaTenhaUmTamanhoInvalidoComValidacaoDeMsg(){

        String placar = "123";

        Assertions.assertThrows(
                PontuacaoComTamanhoInvalidoException.class,
                () -> {
                    try {
                        computaPlacarV01.computaPlacar(placar);
                    } catch (PontuacaoComTamanhoInvalidoException e) {
                        // Verifica a mensagem da exceção lançada
                        String mensagemEsperada = "A string de entrada possui um tamanho inválido! " +
                                "Verifique o input e tente novamente.";
                        Assertions.assertEquals(mensagemEsperada, e.getMessage());
                        throw e; // Re-lança a exceção para manter o comportamento original do assertThrows
                    }
                }
        );
    }

    // --------- [ 02 ] ---------
    @Test
    public void deveRetornarErroCasoOPlacarDeEntradaTenhaCaracteresInvalidosComValidacaoDeMsg(){

        String placar = "00268/5/62816132142%";

        Assertions.assertThrows(
                PontuacaoComCaracteresInvalidosException.class,
                () -> computaPlacarV01.computaPlacar(placar)
        );
    }
    // --------- [ 02.1 ] ---------
    @Test
    public void deveRetornarErroCasoOPlacarDeEntradaTenhaCaracteresInvalidos(){

        String placar = "00268/5/62816132142%";

        Assertions.assertThrows(
                PontuacaoComCaracteresInvalidosException.class,
                () -> {
                    try {
                        computaPlacarV01.computaPlacar(placar);
                    } catch (PontuacaoComCaracteresInvalidosException e) {
                        // Verifica a mensagem da exceção lançada
                        String mensagemEsperada = "A string de entrada possui caracteres inválidos, lembre-se que esse " +
                                "programa só aceita \"X\", \"/\", \"-\" e digitos de 0 a 9.";
                        Assertions.assertEquals(mensagemEsperada, e.getMessage());
                        throw e; // Re-lança a exceção para manter o comportamento original do assertThrows
                    }
                }
        );
    }

    

}
