import audio_to_subtitle_converter as atsc
import srt_writer_reader as swr
import srt_language_translator as slt

#///////////////////////////////////////////////
# // Audio to SRT on same language

def AudioToSRTOnSameLang():
    audio_file_name = "audio"
    audio_language = "en"
    file_name = "output.srt"

    srt_content = atsc.get_large_audio_transcription(audio_file_name,audio_language)
    swr.writeSRTFile(file_name,srt_content,True)


#////////////////////////////////////////////////////
# // Audio to SRT on different languages

def AudioToSRTOnDifferentLang():
    audio_file_name = "audio"
    audio_language = "en"
    to_languages = ["hi"]
    file_name = "output_hindi"

    srt_content = atsc.get_large_audio_transcription(audio_file_name,audio_language)
    swr.writeSRTFile(file_name,srt_content,True)

    slt.srtTranslator(file_name,audio_language,to_languages)


#//////////////////////////////////////////////////////////////
# // SRT to SRT

def SRTToSRT(file_name,from_language,to_languages):
    # file_name = "name"
    # from_language = "lang"
    # to_languages = ["lang1","lang2","lang3"]

    slt.srtTranslator(file_name,from_language,to_languages)


# AudioToSRTOnSameLang()
AudioToSRTOnDifferentLang()