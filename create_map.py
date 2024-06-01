import folium

def create_map():
    m = folium.Map(location=[-15.794229, -47.882166], zoom_start=4)
    m_name = m.get_name()
    # Adiciona o script JavaScript para capturar cliques e enviar para o servidor

    script = f"""
    <script>
    function handleMapClick(e) {{
        var lat = e.latlng.lat;
        var lng = e.latlng.lng;
        fetch('/click_location', {{
            method: 'POST',
            headers: {{
                'Content-Type': 'application/json',
            }},
            body: JSON.stringify({{latitude: lat, longitude: lng}}),
        }})
        .then(response => response.json())
        .then(data => {{
            console.log('Success:', data);
        }})
        .catch((error) => {{
            console.error('Error:', error);
        }});
    }}

    document.addEventListener('DOMContentLoaded', (event) => {{
        var map = window.{m_name};  // Folium map object
        map.on('click', handleMapClick);
    }});
    </script>
    """

    m.get_root().html.add_child(folium.Element(script))

    m.save('templates/mapa.html')


if __name__ == "__main__":
    create_map()
