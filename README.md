# Decodificação do protocolo Ragtech UPS

O objetivo desse projeto é realizar a decodificação do protocolo serial over USB do Ragtech Quad 1200 com Python.

## Por quê?

A Ragtech é uma empresa brasileira de UPS (no-breaks) brasileira que fornece um software proprietário (supervise) para coletar dados através da porta USB disponíveis nos seus dispositivos. A empresa não fornece documentação sobre o protocolo, e o software fornecido possui algumas limitações:
- Roda em computadores com arquitetura AMD64, não suportando ARM64 (Raspberry Pi e outros)
- Disponível para Windows e para Linux, mas com dependências de packages antigos (_libncuses5_ e outros)
- Requer a execução de um serviço para comunicação com o dispositivo
- Expõe esse serviço através de uma interface Web e um API não documentada. Tanto esse serviço quanto a API podem possuir falhas de segurança ainda não exploradas
- Capacidades de notificações limitadas

## Ferramentas

- Sniffer da comunicação através da porta serial
- Arquivo ``devices.xml`` disponível pelo supervise que detalha os baud rates possíveis, bem como o protocolo de cada device
- Python

## Objetivos

- Escrever um código funcional que irá exibir as mesmas informações disponíveis na interface Web do supervise
- Ter o mesmo códgigo disponível para o nodeRED para quem conecta diretamente o USB no host do HA
- Reescrever o código Python em C e adaptar para uso com o nuts
- Permitir que outras pessoas explorem esse código e façam sua própria implementação MQTT
- Ter pessoas que possam usar esse repositório e executar testes nos seus dispositivos
