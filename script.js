const enigmas = [
  { pergunta: "Quanto é 9 + 10?", resposta: "19", nivel: "facil" },
  { pergunta: "Quanto é 15 ÷ 3?", resposta: "5", nivel: "facil" },

  { pergunta: "Qual número completa: 2, 6, 12, 20, ?", resposta: "30", nivel: "medio" },
  { pergunta: "Quanto é metade de 10 + 10?", resposta: "15", nivel: "medio" },

  { pergunta: "Qual número falta: 1, 1, 2, 3, 5, 8, ?", resposta: "13", nivel: "dificil" },
  { pergunta: "Se 5 máquinas fazem 5 peças em 5 minutos, quanto tempo 100 fazem 100?", resposta: "5", nivel: "dificil" }
];

let indice = 0;
let pontos = 0;
let tempo = 10;
let timer;
let jogador = "";

function iniciarJogo() {
  jogador = document.getElementById("nome").value.trim();

  if (jogador === "") {
    alert("Digite seu nome!");
    return;
  }

  document.getElementById("nome").style.display = "none";
  event.target.style.display = "none";

  carregarEnigma();
}

function carregarEnigma() {
  clearInterval(timer);
  tempo = 10;

  let enigma = enigmas[indice];

  document.getElementById("pergunta").innerText =
    `[${enigma.nivel.toUpperCase()}] ` + enigma.pergunta;

  document.getElementById("tempo").innerText = "Tempo: 10s";
  document.getElementById("resposta").value = "";
  document.getElementById("feedback").innerText = "";

  iniciarTimer();
}

function iniciarTimer() {
  timer = setInterval(() => {
    tempo--;
    document.getElementById("tempo").innerText = "Tempo: " + tempo + "s";

    if (tempo <= 0) {
      clearInterval(timer);
      verificar(true);
    }
  }, 1000);
}

function verificar(tempoEsgotado = false) {
  clearInterval(timer);

  let resposta = document.getElementById("resposta").value
    .toLowerCase()
    .trim();

  let correta = enigmas[indice].resposta;

  if (!tempoEsgotado && resposta === correta) {
    pontos += 2;
    document.getElementById("feedback").innerText = "✔️ Acertou!";
    document.getElementById("feedback").style.color = "lime";
  } else {
    document.getElementById("feedback").innerText = "❌ Errado!";
    document.getElementById("feedback").style.color = "red";
  }

  document.getElementById("pontos").innerText = "Pontos: " + pontos;

  indice++;

  if (indice < enigmas.length) {
    setTimeout(carregarEnigma, 1500);
  } else {
    fimDeJogo();
  }
}

function fimDeJogo() {
  salvarPontuacao();

  document.getElementById("jogo").innerHTML =
    `<h2>Fim de jogo!</h2><p>${jogador}, sua pontuação: ${pontos}</p>`;

  mostrarRanking();
}

function salvarPontuacao() {
  let ranking = JSON.parse(localStorage.getItem("ranking")) || [];

  ranking.push({ nome: jogador, pontos: pontos });

  ranking.sort((a, b) => b.pontos - a.pontos);

  ranking = ranking.slice(0, 10);

  localStorage.setItem("ranking", JSON.stringify(ranking));
}

function mostrarRanking() {
  let ranking = JSON.parse(localStorage.getItem("ranking")) || [];

  let html = "<h3>🏆 Ranking</h3>";

  ranking.forEach((j, i) => {
    let medalha = i === 0 ? "🥇" : i === 1 ? "🥈" : i === 2 ? "🥉" : "";
    html += `<p>${medalha} ${i + 1}º - ${j.nome} (${j.pontos})</p>`;
  });

  document.getElementById("ranking").innerHTML = html;
}

mostrarRanking();