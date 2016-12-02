 
    <div class="step">
            <div class="moduleTitle hd">
                    <h2>{$APP.LBL_CR_INVESTOR_PROFILE} - {$APP.LBL_CR_LEGAL_ENTITIES}</h2>
                    <h3>{$APP.LBL_CR_INVESTMENT_GUIDELINES} - {$APP.LBL_CR_STEP} 13</h3>
                    <div class="clear"></div>
            </div>
            <div class="row portfolio-overview">
                    <div class="small-12 column">
                            <p><b>{$APP.LBL_REACTION_BIG_LOSS}</b><br><br>
                            </p>
                            <form class="step_form">
                                    <p>
    <input type="radio" name="reaction_big_loss" value="Ich wuerde die Anlagen sofort verkaufen" {if $data->reaction_big_loss eq "Ich wuerde die Anlagen sofort verkaufen"}checked="checked"{/if}>{$APP.LBL_ANSWER_GIIresult_13_1_TEXT}<br>
    <input type="radio" name="reaction_big_loss" value="Ich wuerde abwarten, dabei aber ein auusserst ungutes Gefuehl haben" {if $data->reaction_big_loss eq "Ich wuerde abwarten, dabei aber ein auusserst ungutes Gefuehl haben"}checked="checked"{/if}>{$APP.LBL_ANSWER_GIIresult_13_2_TEXT}<br>
    <input type="radio" name="reaction_big_loss" value="Ich wuerde investiert bleiben, denn ich rechne mit Phasen von kurzfristiger Volatilitaut" {if $data->reaction_big_loss eq "Ich wuerde investiert bleiben, denn ich rechne mit Phasen von kurzfristiger Volatilitaut"}checked="checked"{/if}>{$APP.LBL_ANSWER_GIIresult_13_3_TEXT}<br>
    <input type="radio" name="reaction_big_loss" value="Ich wuerde zusautzliche Mittel investieren und von den niedrigen Kursen profitieren" {if $data->reaction_big_loss eq "Ich wuerde zusautzliche Mittel investieren und von den niedrigen Kursen profitieren"}checked="checked"{/if}>{$APP.LBL_ANSWER_GIIresult_13_4_TEXT}<br>
                                    </p>
                            </form>
                    </div>
            </div>
            <a href="javascript:void(0)" onclick="SUGAR.RiskWorkflow.next()" data-step="14" class="button gen-button next" >{$APP.LBL_CR_NEXT}</a>
    </div> 
