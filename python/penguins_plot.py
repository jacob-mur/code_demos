from plotnine import (
    ggplot, aes,
    geom_point, geom_smooth,
    facet_wrap,
    scale_color_manual, scale_fill_manual,
    labs, theme_minimal, theme,
    element_text, element_rect, element_line, element_blank
)
from palmerpenguins import load_penguins

"""
plotnine example with custom color pallets
"""

# Load data and drop nas
penguins = load_penguins().dropna()
 
# custom color palette per species
color_dictionary_point = {
    "Adelie": "coral",
    "Chinstrap": "dodgerblue",
    "Gentoo": "darkslategrey",
}

color_dictionary_line = {
    "Adelie": "#FFB89E",
    "Chinstrap": "#59B5F7",
    "Gentoo": "#A1A1A1",
}
 
plot_final = (
    ggplot(penguins, aes(
        x="flipper_length_mm",
        y="body_mass_g",
        color="species",
        fill="species"
    ))
    + geom_point(alpha=0.7, size=2.5, stroke=0.3)
    + geom_smooth(method="lm", alpha=0.15, size=1.2)
    + facet_wrap("~species", ncol=3)
    + scale_color_manual(values=color_dictionary_point)
    + scale_fill_manual(values=color_dictionary_line)
    + labs(
        title="Palmer Penguins: Flipper Length vs Body Mass",
        subtitle="linear fits by species",
        x="Flipper Length (mm)",
        y="Body Mass (g)",
        color="Species",
        fill="Species",
    )
    + theme_minimal(base_size=11)
    + theme(
        plot_title=element_text(face="bold", size=12, margin={"b": 4}),
        plot_subtitle=element_text(size=9, color="#666666", margin={"b": 12}),
        strip_background=element_rect(fill="#F0F4F8", color="none"),
        strip_text=element_text(face="bold", size=10),
        panel_grid_minor=element_blank(),
        panel_grid_major=element_line(color="#E5E5E5"),
        panel_spacing_x = .02,
        legend_position="none", # probably redundant due to faceting
        figure_size=(10, 4),
    )
)

plot_final.show()
