from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtCore import *
from services.korttikube_service import korttikube_service as kks
from config import CARD_RATIO

class CardImage(QWidget):
    """ Class responsible for drawing and saving the card image. """
    
    def __init__(self):
        """ Class constructor. Create a new card image widget and file.
        """
        
        super().__init__()
        self._card_width = 500
        self.setMaximumWidth(self._card_width)
        self.setMaximumHeight(self._card_width*CARD_RATIO)
        self.setMinimumWidth(self._card_width)
        self.setMinimumHeight(self._card_width*CARD_RATIO)
        
        self._frame = ""
        self._card = None

    def set_card(self, card):
        self._card = card

    def _set_card_frame(self):
        """ Sets the frame image png-file path belonging to the card (colour).
        """
        
        self._frame = kks.set_card_frame(self._card)

    def paintEvent(self, event):
        """ QWidget property. Draws text and images on the card frame.
        """
        
        painter = QPainter(self)        
        pen = QPen(3)
        painter.setPen(pen)

        # Card frame
        self._set_card_frame()
        painter.drawPixmap(self.rect(), QPixmap(self._frame))

        # Name
        painter.setFont(QFont("times", 20, QFont.Bold))
        painter.drawText(50,66, self._card.get_name())

        # Maintype, Legendary, Tribal, Subtype
        painter.setFont(QFont("times", 18, QFont.Bold))
        painter.drawText(50,420, self._card.get_legendary_print() + "" + \
                                 self._card.get_tribal_print() + "" + \
                                 self._card.get_maintype() + " – " + \
                                 self._card.get_subtype_print())

        # Manacost
        #400, 66
        flags = Qt.AlignRight
        painter.drawText(300, 40, 150, 40, flags, self._card.get_manacost())

        # Feature, Ruletext, Flavourtext
        painter.setFont(QFont("times", 16))
        flags = Qt.AlignVCenter|Qt.TextWordWrap
        painter.drawText(50, 450, 390, 180, flags, self._card.get_feature_print() + " \n" + \
                                 self._card.get_ruletext() + "\n" + \
                                 self._card.get_flavourtext())

        # Power, Toughness
        if self._card.get_power() is not None:
            painter.setFont(QFont("times", 20, QFont.Bold))
            painter.drawText(400, 652, str(self._card.get_power_print()) + "/" + \
                                      str(self._card.get_toughness_print()))

        # Image
        image = QPixmap(self._card.get_image())
        painter.drawPixmap(43, 83, 416, 306, image)

        # Seticon
        seticon = QPixmap(self._card.get_seticon())
        painter.drawPixmap(425, 398, 30, 30, seticon)

        if self._card.get_colour_print() in ["Musta", "Vihreä"]:
            pen = QPen(Qt.white, 3)
            painter.setPen(pen)

        # Rarity
        painter.setFont(QFont("times", 12))
        painter.drawText(150,670, self._card.get_rarity())

        # Creator
        painter.drawText(50,670, self._card.get_creator())
        painter.end()

    def save_image(self):
        """ Creates and returns a QPixmap of the image.
            p: [QPixmap] Picture widget of the image.
        """

        p = QPixmap(self.size())
        self.render(p)

        return p