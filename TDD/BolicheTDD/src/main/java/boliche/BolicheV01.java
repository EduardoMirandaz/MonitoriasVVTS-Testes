package boliche;

import exception.ExceptionMessageUtils;
import exception.PontuacaoComCaracteresInvalidosException;
import exception.PontuacaoComTamanhoInvalidoException;

public class BolicheV01 {

    // Aqui, na versão 1 do ComputaPlacar, espera-se do conversor que
    // a formatação da entrada estará perfeita e pronta para a realização
    // das operações matemáticas.

    public int computaPlacar(String strPlacarDeEntrada) throws PontuacaoComTamanhoInvalidoException, PontuacaoComCaracteresInvalidosException {
        validarTamanhoDaStringPlacar(strPlacarDeEntrada);
        validarCaracteresDaStringPlacar(strPlacarDeEntrada);
        return 0;
    }

    private void validarTamanhoDaStringPlacar(String strPlacarDeEntrada) throws PontuacaoComTamanhoInvalidoException {
        if(strPlacarDeEntrada.length() < 20 || strPlacarDeEntrada.length() > 21) {
            String errorMessage = ExceptionMessageUtils.getMessage("pontuacao.com.tamanho.invalido.message");
            throw new PontuacaoComTamanhoInvalidoException(errorMessage);
        }
    }

    private void validarCaracteresDaStringPlacar(String strPlacarDeEntrada) throws PontuacaoComCaracteresInvalidosException {
        String pattern = "^[X\\-\\d/]*$";
        if (!strPlacarDeEntrada.matches(pattern)) {
            String errorMessage = ExceptionMessageUtils.getMessage("pontuacao.com.caracteres.invalidos.message");
            throw new PontuacaoComCaracteresInvalidosException(errorMessage);
        }

    }

}
